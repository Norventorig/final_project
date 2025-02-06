from site_api.core import site_api_handler


class IMDBDataHandler:
    media_id = 1
    processing_func = site_api_handler.get_movie_by_id


imdb_data_handler = IMDBDataHandler()
