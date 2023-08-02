import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from testing_requests import (
    async_native as an,
    async_multi_session as ams,
    async_one_session as aos,
    sync_http_request as shr,
    settings
)

urls = settings.URLS


shr.default(urls)
asyncio.run(an.async_native(urls))
asyncio.run(ams.multi_session(urls))
asyncio.run(aos.one_session_check(urls))
