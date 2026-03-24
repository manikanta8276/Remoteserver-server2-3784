from fastmcp import FastMCP
import random
import json
#create 
mcp=FastMCP("Simple Caluculator server 2")
#tool
@mcp.tool
def add(a:int,b:int)->int:
    """Add two Number Together
    Args :
    a:First Number
    b:second Number
    Returns :
    The Sum of a and b
    """
    return a+b
#----------------------------------#tool:Generate a random number -------------------
@mcp.tool
def random_number(min_val:int=1,max_val:int=100)->int:
    """Generate A random Number Within Range
    Args :
    min_val:Minimum Value (default:1)
    max_val:maximum value (default:100)
    returns:
    A Random interger between min_val and max_val"""
    return random.randint(min_val,max_val)
#@resource
@mcp.resource("info://server")
def server_info()->str:
    """Get the information about This server"""
    info={
        "name":"Simple cal",
        "version":"1.0.0",
        "descripition":"A Basic Mcp Server with math tools",
        "tools":["add","random_number"],
        "another":"your name "

    }
    return json.dumps(info,indent=2)



if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
#-----------------------------------------------------------------------------------------------------------
#deply in git hub then server 

