from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route 

async def homepage(request):
    return JSONResponse({"message": "Hello, Starlette!"})   

async def other_endpoint(request):
    return JSONResponse({"message": "This is another endpoint."})   

app = Starlette(debug=True,routes=[
    Route("/", homepage)    
])
app.add_route("/other", other_endpoint)    
    
    
# To run the application, use the command:
# uvicorn starlette_basic.main:app --reload