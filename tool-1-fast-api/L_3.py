from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional

app = FastAPI()

class AddRequest(BaseModel):  #making it clear how the data type will be
    A: int
    B: int
    label: Optional[str] = None

@app.post("/add")
def add(data: AddRequest):
    result = data.A + data.B
    if data.label:
        return{"result": result, "label": data.label}
    return{"result": result}