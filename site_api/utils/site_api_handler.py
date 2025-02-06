import requests
from settings import site_settings


def _make_response(method: str, url: str, timeout: int, success=200):
    headers = {
        'X-RapidAPI-Key': site_settings.rapidapi_key.get_secret_value(),
        'X-RapidAPI-Host': site_settings.rapidapi_host.get_secret_value()
    }

    response = requests.request(method=method,
                                url=url,
                                headers=headers,
                                timeout=timeout)

    if response.status_code == success:
        return response

    return response.status_code


def _get_100_movies(timeout=10, func=_make_response):
    method = 'get'
    url = site_settings.base_url.get_secret_value()

    return func(method=method,
                url=url,
                timeout=timeout)


def _get_100_series(timeout=10, func=_make_response):
    method = 'get'
    url = site_settings.series.get_secret_value()

    return func(method=method,
                url=url,
                timeout=timeout)


def _get_movie_by_id(top: int, timeout: int = 10, func=_make_response):
    method = 'get'
    url = site_settings.movie_data.get_secret_value().format(top)

    return func(method=method,
                url=url,
                timeout=timeout)


def _get_series_by_id(top: int, timeout: int = 10, func=_make_response):
    method = 'get'
    url = site_settings.series_data.get_secret_value().format(top)

    return func(method=method,
                url=url,
                timeout=timeout)


class SiteAPIHandler:
    @staticmethod
    def get_100_movies():
        return _get_100_movies()

    @staticmethod
    def get_100_series():
        return _get_100_series()

    @staticmethod
    def get_movie_by_id(top: int = 1):
        return _get_movie_by_id(top=top)

    @staticmethod
    def get_series_by_id(top: int = 1):
        return _get_series_by_id(top=top)
