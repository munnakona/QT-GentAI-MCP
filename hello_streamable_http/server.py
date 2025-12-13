from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Mount,Host

from mcp.server.fastmcp  import FastMCP

mcp = FastMCP("sse-starlette")

@mcp.tool()
def add(x: int, y: int) -> int:
    return x + y
@mcp.tool()
def echo(message: str) -> str:
    return f"{message}"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")