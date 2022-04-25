import uvicorn
from fastapi import FastAPI

from app.settings import get_settings
from app.routers import healthcheck, model 


settings = get_settings()
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description
)

app.include_router(healthcheck.router)
app.include_router(model.router)


@app.get("/")
async def root():
    """
        Load the project name as a message on the API root route.
    """
    return {"message": settings.app_name}


if __name__ == "__main__":
    uvicorn.run(app, log_level="info")
