from fastapi import FastAPI  

app = FastAPI() 

@app.get("/hello")
def hello():
    return{"message" : "Hello World"}

@app.post("/input")
def input(a: int, b: int):
    return{"result" : a+b}





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

#app.post: Listens for POST requests (standard for sending data to the server).
#("/add"): The URL path for this endpoint.
#add: Name of the function.
#a: int: Defines a parameter named a. The : int part is type hinting. FastAPI uses this to:
#1.  Read the value from the query string (e.g., ?a=5&b=10).
#2. Automatically validate that it is an integer.
#3. Convert it to an integer if possible.
#b: int: Same logic for parameter b.

#a + b: Performs the addition of the two integers.
#{"result": ...}: Wraps the calculation in a dictionary to be returned as JSON.
#uvicorn main:app --reload     main: The filename (without .py).  app: The variable name defined in the code (app = FastAPI()).
#--reload: Automatically restarts the server when you change the code.
