import requests
from ..config.data_reader import get


def _get(url: str = '', number: int = 1) -> object:
    url = get(url).format(number)
    headers = get('headers')

    response = requests.get(url=url, headers=headers)

    return response


class SiteApiInterfacer:
    @staticmethod
    def get_movies() -> object:
        return _get(url='base_url')

    @staticmethod
    def get_series() -> object:
        return _get(url='series')

    @staticmethod
    def get_series_data(number: int) -> object:
        return _get(url='series_data', number=number)

    @staticmethod
    def get_movie_data(number: int) -> object:
        return _get(url='movie_data', number=number)
