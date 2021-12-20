import datetime


def speed_test(func):
    async def wrapper(*args, **kwargs):
        start = datetime.datetime.now()

        original_result = await func(*args, **kwargs)

        end = datetime.datetime.now()
        print(end - start)
        return original_result
    return wrapper
