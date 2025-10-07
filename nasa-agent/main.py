import uvicorn

from client import Client
from fastapi import FastAPI

app = FastAPI()
client = Client()

@app.get("/health")
def health():
  return {"status": "ok"}


@app.get("/picture-of-the-day")
def picture_of_the_day():
  return client.get_picture_of_the_day()


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)
