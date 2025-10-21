from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Model to define the input structure
class Numbers(BaseModel):
    num1: float
    num2: float

# ➕ Endpoint for addition
@router.post("/sum")
def get_sum(data: Numbers):
    return {"sum": data.num1 + data.num2}

# ➖ Endpoint for subtraction
@router.post("/subtract")
def get_subtract(data: Numbers):
    return {"difference": data.num1 - data.num2}
