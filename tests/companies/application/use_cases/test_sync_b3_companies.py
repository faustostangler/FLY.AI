import pytest
from datetime import datetime
from unittest.mock import MagicMock
from companies.application.use_cases.sync_b3_companies import SyncB3CompaniesUseCase


class TestSyncB3CompaniesUseCase:
    @pytest.fixture
    def use_case(self):
        data_source = MagicMock()
        repository = MagicMock()
        telemetry = MagicMock()
        return SyncB3CompaniesUseCase(data_source, repository, telemetry)

    @pytest.mark.asyncio
    async def test_process_single_company_errors(self, use_case):
        from shared.infrastructure.progress import ProgressReporter
        import asyncio
        from companies.domain.exceptions import (
            B3RateLimitExceededError,
            CompanyValidationError,
            CompanyDataValidationError,
            B3NetworkTimeoutError,
        )
        from unittest.mock import AsyncMock, patch

        reporter = ProgressReporter(total=1)
        sem = asyncio.Semaphore(1)

        # 1. Missing ticker/cvm -> DataValidation Error
        res_missing = await use_case._process_single_company(
            0, {"issuingCompany": ""}, sem, reporter
        )
        assert res_missing.is_failure
        assert isinstance(res_missing.error, CompanyDataValidationError)

        # 2. Rate Limit Exceeded
        use_case._data_source.fetch_company_details = AsyncMock(
            side_effect=B3RateLimitExceededError("Limit")
        )
        res_limit = await use_case._process_single_company(
            0, {"issuingCompany": "PETR4", "codeCVM": "9512"}, sem, reporter
        )
        assert res_limit.is_failure
        assert isinstance(res_limit.error, B3RateLimitExceededError)

        # 3. Timeout
        use_case._data_source.fetch_company_details = AsyncMock(
            side_effect=asyncio.TimeoutError()
        )
        res_timeout = await use_case._process_single_company(
            0, {"issuingCompany": "VALE3", "codeCVM": "4170"}, sem, reporter
        )
        assert res_timeout.is_failure
        assert isinstance(res_timeout.error, B3NetworkTimeoutError)

        # 4. Generic Exception
        use_case._data_source.fetch_company_details = AsyncMock(
            side_effect=Exception("Generic Error")
        )
        res_generic = await use_case._process_single_company(
            0, {"issuingCompany": "ITUB4", "codeCVM": "19348"}, sem, reporter
        )
        assert res_generic.is_failure
        assert isinstance(res_generic.error, Exception)
        assert not isinstance(res_generic.error, CompanyValidationError)

        # 5. Domain logic validation error (from Mapper)
        use_case._data_source.fetch_company_details = AsyncMock(
            return_value={"details": "dummy"}
        )
        with patch("companies.application.use_cases.sync_b3_companies.B3CompanyMapper.to_domain") as mock_mapper:
            mock_mapper.side_effect = CompanyValidationError("Domain Logic Fail", "ticker")
            res_domain = await use_case._process_single_company(
                0, {"issuingCompany": "WEGE3", "codeCVM": "123"}, sem, reporter
            )
            assert res_domain.is_failure
            assert isinstance(res_domain.error, CompanyValidationError)

        # 6. Pydantic ValidationError (from Mapper)
        from pydantic import ValidationError
        
        # Helper to get a real ValidationError
        def raise_val_error():
            from companies.application.dtos.b3_company_dto import B3CompanyPayloadDTO
            B3CompanyPayloadDTO() # missing fields

        validation_error = None
        try:
            raise_val_error()
        except ValidationError as e:
            validation_error = e

        with patch("companies.application.use_cases.sync_b3_companies.B3CompanyMapper.to_domain") as mock_mapper:
            mock_mapper.side_effect = validation_error
            res_pydantic = await use_case._process_single_company(
                0, {"issuingCompany": "B3SA3", "codeCVM": "1234"}, sem, reporter
            )
            assert res_pydantic.is_failure
            assert isinstance(res_pydantic.error, CompanyDataValidationError)
            assert res_pydantic.error.field == "multiple"

        # 7. Happy path
        company_mock = MagicMock()
        company_mock.ticker = "BBAS3"
        with patch("companies.application.use_cases.sync_b3_companies.B3CompanyMapper.to_domain", return_value=company_mock):
            res_success = await use_case._process_single_company(
                0, {"issuingCompany": "BBAS3", "codeCVM": "789"}, sem, reporter
            )
            assert res_success.is_success
            assert res_success.value == company_mock


    @pytest.mark.asyncio
    async def test_execute_orchestration_mixed_results(self, use_case):
        from unittest.mock import AsyncMock
        from shared.domain.utils.result import Result
        from companies.domain.exceptions import (
            B3RateLimitExceededError,
            CompanyDataValidationError,
            CompanyValidationError,
            B3NetworkTimeoutError,
        )

        # We'll mock out the data_source async context manager
        use_case._data_source.__aenter__ = AsyncMock(return_value=None)
        use_case._data_source.__aexit__ = AsyncMock(return_value=None)

        # Fetch initial will return items covering all telemetry paths
        use_case._data_source.fetch_initial_companies = AsyncMock(
            return_value=[
                {"issuingCompany": "PETR4", "codeCVM": "9512"},
                {"issuingCompany": "VALE3", "codeCVM": "4170"},
                {"issuingCompany": "ITUB4", "codeCVM": "123"},
                {"issuingCompany": "WEGE3", "codeCVM": "456"},
                {"issuingCompany": "ABEV3", "codeCVM": "789"},
                {"issuingCompany": "B3SA3", "codeCVM": "000"},
            ]
        )

        class DummyCompany:
            def __init__(self, ticker):
                self.ticker = ticker

        c1 = DummyCompany("PETR4")

        async def mock_process(index, raw, sem, reporter):
            t = raw.get("issuingCompany")
            if t == "PETR4":
                return Result.ok(c1)
            elif t == "VALE3":
                return Result.fail(CompanyDataValidationError("Err", "field", "VALE3"))
            elif t == "ITUB4":
                return Result.fail(CompanyValidationError("Err", "field"))
            elif t == "WEGE3":
                return Result.fail(B3RateLimitExceededError("Limit"))
            elif t == "ABEV3":
                return Result.fail(B3NetworkTimeoutError("Timeout"))
            else:
                return Result.fail(Exception("Generic"))

        use_case._process_single_company = mock_process

        await use_case.execute()

        # Persistence check
        use_case._repository.save_batch.assert_called_once()
        saved_entities = use_case._repository.save_batch.call_args[0][0]
        assert len(saved_entities) == 1
        assert saved_entities[0].ticker == "PETR4"

        # Telemetry verification
        use_case._telemetry.increment_active_sync_tasks.assert_called_once()
        use_case._telemetry.decrement_active_sync_tasks.assert_called_once()
        use_case._telemetry.increment_data_validation_error.assert_any_call(
            entity="Company", field="field", reason="b3_payload_mismatch"
        )
        use_case._telemetry.increment_data_validation_error.assert_any_call(
            entity="Company", field="domain_logic", reason="business_rule_violation"
        )
        use_case._telemetry.increment_b3_rate_limit_hits.assert_called_once()
        use_case._telemetry.increment_generic_sync_error.assert_any_call(
            type="NetworkTimeout"
        )
        use_case._telemetry.increment_generic_sync_error.assert_any_call(
            type="Exception"
        )

        use_case._telemetry.increment_companies_synced.assert_any_call(
            count=1, status="success"
        )
        use_case._telemetry.increment_companies_synced.assert_any_call(
            count=5, status="failed"
        )
