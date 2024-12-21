from fastapi import FastAPI
from app.routes import sms

# Create FastAPI app
app = FastAPI(title="SMS Service Framework")

# Register routes
app.include_router(sms.router, prefix="/api")

@app.on_event("startup")
async def print_routes():
    for route in app.routes:
        print(route.path)
