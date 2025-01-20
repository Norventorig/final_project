import os

from dotenv import load_dotenv
from pydantic import SecretStr, StrictStr
from pydantic_settings import BaseSettings

load_dotenv()


class SiteSettings(BaseSettings):
    base_url: SecretStr = os.getenv('BASE_URL')
    movie_data: SecretStr = os.getenv('MOVIE_DATA')
    series: SecretStr = os.getenv('SERIES')
    series_data: SecretStr = os.getenv('SERIES_DATA')
    rapidapi_key: SecretStr = os.getenv('X-RAPIDAPI-KEY')
    rapidapi_host: SecretStr = os.getenv('X-RAPIDAPI-HOST')
