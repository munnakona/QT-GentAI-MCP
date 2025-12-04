from mcp.server.fastmcp import FastMCP
mcp = FastMCP(name = 'calc-mcp')

@mcp.tool()
def substract(a: int | float, b: int | float) -> int | float:
    """This method subtracts two numbers

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int | float: a - b
    """
    return a - b

@mcp.tool()
def multiply(a: int | float, b: int | float) -> int | float:
    """This method multiplies two numbers

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int | float: a * b
    """
    return a * b    

@mcp.tool()
def divide(a: int | float, b: int | float) -> int | float:
    """This method divides two numbers

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int | float: a / b
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b        