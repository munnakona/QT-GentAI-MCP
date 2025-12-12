from starlette.applications import Starlette # Import the Starlette application class
from starlette.responses import JSONResponse # Import JSONResponse to send JSON responses
from starlette.routing import Route # Import Route to define application routes

async def homepage(request): # Define an asynchronous function for the homepage endpoint
    return JSONResponse({"message": "Hello, Starlette!"}) # Return a JSON response with a greeting message

async def other_endpoint(request): # Define another asynchronous function for a different endpoint
    return JSONResponse({"message": "This is another endpoint."})# Return a JSON response for the other endpoint

# Create the Starlette application and define routes
app = Starlette(debug=True,routes=[
    Route("/", homepage)    
])
# Add another route to the application
app.add_route("/other", other_endpoint)    
    
    
# To run the application, use the command: uvicorn main:app 
# uvicorn starlette_basic.main:app --reload