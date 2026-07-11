from ast import If

from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

class AddRequest(BaseModel):  #making it clear how the data type will be
    A: int
    B: int

@app.post("/add")
def add(data: AddRequest):
    return{"result": data.A + data.B}



#Parsing: FastAPI sees the payload: AddRequest argument. It takes the raw JSON string and passes it to Pydantic.
#Validation: Pydantic checks if the JSON has keys a and b.
    #It checks if a and b are integers.
    #If invalid (e.g., {"a": "ten", "b": 5}), it stops immediately and returns a 422 error with details on what went wrong.
#Execution: If valid, Pydantic creates an AddRequest object and passes it to the add function.
#Logic: The function calculates 10 + 5.
#Response: The function returns {"result": 15}. 
#FastAPI converts this to a JSON string and sends it back to the client with a 200 OK status.


#from pydantic import BaseModel: Imports BaseModel from the pydantic library. 
    # Pydantic is used for data validation and settings management using Python type annotations. 
    # In FastAPI, this is the standard way to define the structure of data sent in the request body.

#app: The variable name holding your application instance.
#FastAPI(): Instantiates the application. The () is crucial; it creates the object.

#class: Defines a new Python class.
#AddRequest: The name of the class. By convention, request models often end in "Request" or "Body".
#(BaseModel): Inheriting from BaseModel tells Pydantic to validate any data passed to this class.
#A: int: Defines a field named A that must be an integer.
#B: int: Defines a field named B that must be an integer.
#How it works: If the incoming JSON data is missing A, B, or if A is a string like "five", 
    # Pydantic will automatically raise a 422 Unprocessable Entity error with a helpful message, 
    # preventing the function from running.

#data: The name of the argument receiving the data. You can name this anything, but payload or data is common.
#data: AddRequest: This is the critical part. It tells FastAPI:
    #"Expect the request body to be JSON."
    #"Parse that JSON into an AddRequest object."
    #"Validate it against the a and b integer rules defined earlier."
    #"Pass the validated object to this function as payload."