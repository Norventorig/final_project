from settings import site_settings
from site_api.utils.site_api_handler import SiteAPIHandler


site_api_handler = SiteAPIHandler(host=site_settings.rapidapi_host.get_secret_value(),
                                  key=site_settings.rapidapi_key.get_secret_value(),
                                  get_100_movies_url=site_settings.base_url.get_secret_value(),
                                  get_100_series_url=site_settings.series.get_secret_value(),
                                  get_movie_by_id_url=site_settings.movie_data.get_secret_value(),
                                  get_series_by_id_url=site_settings.series_data.get_secret_value())
