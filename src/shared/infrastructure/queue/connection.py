from arq import create_pool
from arq.connections import RedisSettings as ArqRedisSettings
from shared.infrastructure.config import settings

# Global connection pool instance
_redis_pool = None


async def get_arq_redis_pool():
    """Dependency provider for ARQ Redis dispatcher.
    
    Creates a singleton pool that respects settings.redis canonical attributes.
    """
    global _redis_pool
    if _redis_pool is None:
        arq_redis_settings = ArqRedisSettings(
            host=settings.redis.host,
            port=settings.redis.port,
            database=settings.redis.db,
        )
        _redis_pool = await create_pool(arq_redis_settings)
    
    return _redis_pool
