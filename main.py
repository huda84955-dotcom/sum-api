from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/sum")
def get_sum(data: Numbers):
    return {"sum": data.num1 + data.num2}
