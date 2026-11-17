from fastapi import FastAPI

from app.api.routes import hosts


app = FastAPI(
    title="Infrastructure Monitor API",
    description="API for monitoring infrastructure resources",
    version="0.1.0",
)


app.include_router(
    hosts.router,
    prefix="/api/v1",
)


@app.get("/")
def root():
    return {
        "message": "Infrastructure Monitor API is running",
        "status": "online",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }