from fastapi import FastAPI

app = FastAPI(
    title="Infrastructure Monitor API",
    description="API for monitoring infrastructure resources",
    version="0.1.0",
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