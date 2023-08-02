from testing_requests import time_decoratos as td
import requests


@td.time_check
def default(urls: list[str]):
    for i in urls:
        _ = requests.get(i)


if __name__ == '__main__':
    import settings
    default(settings.URLS)