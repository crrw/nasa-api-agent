import os
from dotenv import load_dotenv

class NasaApiConfig:
  """
    loads and stores NASA Api configs
  """

  def __init__(self):
    load_dotenv()
    self.api_key = os.getenv("API_KEY")
    self.base_url = "https://api.nasa.gov/"
