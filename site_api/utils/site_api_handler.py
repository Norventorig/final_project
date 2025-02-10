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


class SiteAPIHandler:
    def __init__(self,
                 host: str,
                 key: str,
                 get_100_movies_url: str,
                 get_100_series_url: str,
                 get_movie_by_id_url: str,
                 get_series_by_id_url: str):

        self.host = host
        self.key = key
        self.get_100_movies_url = get_100_movies_url
        self.get_100_series_url = get_100_series_url
        self.get_movie_by_id_url = get_movie_by_id_url
        self.get_series_by_id_url = get_series_by_id_url

    def get_100_movies(self):
        return _make_response(method='get',
                              url=self.get_100_movies_url,
                              timeout=10,
                              host=self.host,
                              key=self.key)

    def get_100_series(self):
        return _make_response(method='get',
                              url=self.get_100_series_url,
                              timeout=10,
                              host=self.host,
                              key=self.key)

    def get_movie_by_id(self, top: int = 1):
        return _make_response(method='get',
                              url=self.get_movie_by_id_url.format(top),
                              timeout=10,
                              host=self.host,
                              key=self.key)

    def get_series_by_id(self, top: int = 1):
        return _make_response(method='get',
                              url=self.get_series_by_id_url.format(top),
                              timeout=10,
                              host=self.host,
                              key=self.key)
