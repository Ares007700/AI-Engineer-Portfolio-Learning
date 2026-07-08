from fastapi import FastAPI  

app = FastAPI()   
@app.get("/hello")
def hello():
    return{"message" : "Hello World"}


#from fastapi: Tells Python to look inside the installed fastapi library
#import FastAPI: Brings the main FastAPI class into your script so you can use it
#app: The name you give to your application instance (can be anything, e.g., weather)
#=: Assigns the new instance to the variable
#FastAPI(): Creates a new instance of the FastAPI application. The parentheses () are required to actually create the object
#@: Indicates a decorator. This is a Python feature that modifies the function below it
#app.get: Tells FastAPI to listen for GET requests (standard for retrieving data)
#("/hello"): The path or URL endpoint. If the user visits http://yourserver/hello, this function runs
#def: Stands for "define," used to create a standard Python function
#hello: The name of the function
#(): No input parameters are needed for this specific endpoint
#:: Starts the function block
#return: Sends data back to the user
#{"message": "Hello world"}: A Python dictionary. FastAPI automatically converts this into JSON format for the response
#