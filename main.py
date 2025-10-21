from fastapi import FastAPI
from routers import calculator  # Import the router file

app = FastAPI(title="Sum and Subtract API", description="Simple API to add and subtract numbers", version="1.0")

# Connect your router to the app
app.include_router(calculator.router)
