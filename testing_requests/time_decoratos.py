import time
import logging
import os


log_name = f'requests.txt'

if os.path.exists(log_name):
    os.remove(log_name)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(message)s")

file_handler = logging.FileHandler(log_name, 'a')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def time_check(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        result = func(*args, **kwargs)
        e = time.time()
        logger.debug(msg=f'{func.__name__} : {e-s}')
        return result
    return wrapper


def time_check_async(func):
    async def wrapper(*args, **kwargs):
        s = time.time()
        result = await func(*args, **kwargs)
        e = time.time()
        logger.debug(msg=f'{func.__name__} : {e-s}')
        return result
    return wrapper


if __name__ == '__main__':
    @time_check
    def test():
        import time
        time.sleep(1)

    test()