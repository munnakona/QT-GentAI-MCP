from mcp.server.fastmcp import FastMCP

# creating a server
mcp = FastMCP("hello-mcp")

# define tools
@mcp.tool()
def add(a:int|float, b:int|float) -> int|float:
    """This method adds two numbers

    Args:
        a (int | float): number 
        b (int | float): number

    Returns:
        int|float: a + b
    """
    return a + b

# define resources

@mcp.resource(uri="data://operations") #list of available operations
def operations() -> list[str]: # list of available operations
    return ["add", "sub", "mul", "div"] # returning list of operations


@mcp.resource(uri="data://operation/{intent}") # get operation details based on intent
def get_operation(intent:str) -> str: # get operation details based on intent 
    if intent == "add": # if intent is add  
        return "add" # return add operation
    else:   #   
        return "idont know" # return idont know for other intents
    
    
if __name__ == "__main__": # run the server
    mcp.run(transport="stdio") # run the server with stdio transport
