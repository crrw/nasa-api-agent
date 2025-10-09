import mcp.cli.cli
import uvicorn

from client import Client
from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

app = FastAPI()
client = Client()
mcp = FastMCP()

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/picture-of-the-day")
def picture_of_the_day():
    return client.get_picture_of_the_day()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    mcp.run(transport="sse", port=8080)
