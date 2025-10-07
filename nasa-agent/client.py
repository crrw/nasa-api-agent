import requests

from config import NasaApiConfig

class Client:

  def __init__(self, config: NasaApiConfig = None):
    self.config = config or NasaApiConfig()

  def get_picture_of_the_day(self):
    """
    Fetch NASA Astronomy picture of the day
    """
    endpoint = f"{self.config.base_url}planetary/apod"
    params = {"api_key": self.config.api_key}

    response = requests.get(endpoint, params=params)
    response.raise_for_status()

    return response.json()