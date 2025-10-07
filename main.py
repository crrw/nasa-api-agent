import os

from fastapi import FastAPI
from dotenv import load_dotenv

API_KEY = os.getenv("API_KEY")
APP = FastAPI()
URI = "https://api.nasa.gov/"

@APP.get("/")
def health():
  return {"hello": "world"}

def picture_of_the_day():
  pass
