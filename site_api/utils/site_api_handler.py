import requests


def _make_response(method: str, url: str, timeout: int, host: str, key: str, success=200):
    headers = {
        'X-RapidAPI-Key': key,
        'X-RapidAPI-Host': host
    }

    response = requests.request(method=method,
                                url=url,
                                headers=headers,
                                timeout=timeout)

    if response.status_code == success:
        return response

    return response.status_code


def _get_100_movies(url: str, host: str, key: str, timeout: int = 10, func=_make_response):
    method = 'get'

    return func(method=method,
                url=url,
                timeout=timeout,
                host=host,
                key=key)


def _get_100_series(url: str, host: str, key: str, timeout: int = 10, func=_make_response):
    method = 'get'

    return func(method=method,
                url=url,
                timeout=timeout,
                host=host,
                key=key)


def _get_movie_by_id(url: str, host: str, key: str, top: int, timeout: int = 10, func=_make_response):
    method = 'get'
    url = url.format(top)

    return func(method=method,
                url=url,
                timeout=timeout,
                host=host,
                key=key)


def _get_series_by_id(url: str, host: str, key: str, top: int, timeout: int = 10, func=_make_response):
    method = 'get'
    url = url.format(top)

    return func(method=method,
                url=url,
                timeout=timeout,
                host=host,
                key=key)


class SiteAPIHandler:
    @staticmethod
    def get_100_movies(url: str, host: str, key: str):
        return _get_100_movies(url=url,
                               host=host,
                               key=key)

    @staticmethod
    def get_100_series(url: str, host: str, key: str):
        return _get_100_series(url=url,
                               host=host,
                               key=key)

    @staticmethod
    def get_movie_by_id(url: str, host: str, key: str, top: int = 1):
        return _get_movie_by_id(top=top, url=url,
                                host=host,
                                key=key)

    @staticmethod
    def get_series_by_id(url: str, host: str, key: str, top: int = 1):
        return _get_series_by_id(top=top, url=url,
                                 host=host,
                                 key=key)
