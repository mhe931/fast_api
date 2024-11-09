from fastapi import FastAPI
from routes import dkg_data
from auth import auth  # Import the auth module

app = FastAPI()

# Include the routers
app.include_router(dkg_data.router, prefix="/api")
app.include_router(auth.router)  # Add the auth router

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
