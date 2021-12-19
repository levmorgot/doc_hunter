import json
import functools
import aioredis


def redis_cache(key: str, ex: int):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            redis = aioredis.from_url(
                "redis://localhost", encoding="utf-8", decode_responses=True
            )
            async with redis.client() as conn:
                cache = await conn.get(f"{key}{args[1:]}")
                if cache is not None:
                    value = json.loads(cache)
                    return value
            fresh_result = await func(*args, **kwargs)

            async with redis.client() as conn:
                await conn.set(f"{key}{args[1:]}", json.dumps(fresh_result), ex=ex)

            return fresh_result

        return wrapper
    return decorator
