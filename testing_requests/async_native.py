import aiohttp
from testing_requests import time_decoratos as td


@td.time_check_async
async def async_native(urls):
    sessions = [aiohttp.ClientSession() for _ in urls]
    _ = [await y.get(x) for x, y in zip(urls, sessions)]

    _ = [await x.close() for x in sessions]