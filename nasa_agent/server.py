from mcp.server.fastmcp import FastMCP
from client import Client

mcp = FastMCP("Nasa Service")
client = Client()

'''
This class serves as a 'hello world' test
'''

@mcp.tool()
def get_picture_of_the_day():
  """Get the picture for today"""
  return client.get_picture_of_the_day()

@mcp.resource("picture://")
def resource():
  """Provide today's picture as a resource"""
  return f"Today's picture of the day is: {client.get_picture_of_the_day()}"

@mcp.prompt()
def prompt():
  """Create a picture of the day prompt"""
  return "What is the picture for today?"

if __name__ == '__main__':
    mcp.run()
