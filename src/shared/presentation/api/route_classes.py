import time
import uuid
import structlog
from typing import Callable, Any
from fastapi import Request, Response
from fastapi.routing import APIRoute

from shared.infrastructure.monitoring import metrics


class SRETelemetryRoute(APIRoute):
    """Custom APIRoute to correctly capture Prometheus metrics without Cardinality Explosion.
    
    FastAPI middlewares run before routing is complete. Thus, requesting request.scope['route']
    returns None and forces fallbacks to request.url.path, exploding TSDB cardinality.
    This APIRoute runs *after* routing, providing direct access to self.path (the templated route).
    """

    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            method = request.method
            # Extracted matched template (e.g., /api/v1/companies/{ticker}) instead of raw URL
            path = self.path

            # 0. TRACEABILITY: Extract ID from LB (Nginx/Traefik) or generate fallback.
            request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
            structlog.contextvars.clear_contextvars()
            structlog.contextvars.bind_contextvars(
                http_method=method,
                path=path,
                request_id=request_id,
            )

            # 1. SATURATION/CONCURRENCY: Track active requests.
            metrics.IN_FLIGHT_REQUESTS.labels(method=method, endpoint=path).inc()

            start_time = time.perf_counter()

            # 2. TRAFFIC: Inbound payload measurement.
            content_length_str = request.headers.get("content-length")
            if content_length_str:
                try:
                    req_size = int(content_length_str)
                    metrics.HTTP_REQUEST_SIZE.labels(method=method, endpoint=path).observe(req_size)
                    metrics.NETWORK_TRANSMIT_BYTES_TOTAL.labels(
                        direction="inbound", context="api"
                    ).inc(req_size)
                except ValueError:
                    structlog.get_logger().warning(
                        "security_anomaly_detected",
                        anomaly_type="invalid_content_length",
                        value=content_length_str,
                        direction="inbound",
                    )

            try:
                # Proceed to actual route dependencies and logic
                response: Response = await original_route_handler(request)
                
                duration = time.perf_counter() - start_time
                status_code = str(response.status_code)

                # 3. LATENCY & THROUGHPUT: Observe performance per endpoint/status.
                metrics.HTTP_REQUEST_DURATION.labels(method=method, endpoint=path).observe(duration)
                metrics.HTTP_REQUESTS_TOTAL.labels(
                    method=method, endpoint=path, status=status_code
                ).inc()

                # 4. TRAFFIC: Outbound payload measurement.
                out_content_length = response.headers.get("content-length")
                if out_content_length:
                    try:
                        resp_size = int(out_content_length)
                        metrics.HTTP_RESPONSE_SIZE.labels(method=method, endpoint=path).observe(resp_size)
                        metrics.NETWORK_TRANSMIT_BYTES_TOTAL.labels(
                            direction="outbound", context="api"
                        ).inc(resp_size)
                    except ValueError:
                        structlog.get_logger().warning(
                            "security_anomaly_detected",
                            anomaly_type="invalid_content_length",
                            value=out_content_length,
                            direction="outbound",
                        )

                # 5. ERRORS: Track non-2xx status codes for SLI calculation.
                if response.status_code >= 400:
                    metrics.HTTP_REQUESTS_FAILED_TOTAL.labels(
                        method=method, endpoint=path, error_type=status_code
                    ).inc()

                # 6. TRACEABILITY: Ensure the ID is propagated back to the client.
                response.headers["X-Request-ID"] = request_id

                return response

            except Exception as e:
                # Track unhandled exceptions as critical errors (Type 500 equivalent).
                metrics.HTTP_REQUESTS_FAILED_TOTAL.labels(
                    method=method, endpoint=path, error_type=type(e).__name__
                ).inc()
                raise e

            finally:
                # Decrement concurrency gauge to maintain mathematical consistency.
                metrics.IN_FLIGHT_REQUESTS.labels(method=method, endpoint=path).dec()

        return custom_route_handler
