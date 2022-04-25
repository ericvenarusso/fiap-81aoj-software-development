from fastapi import APIRouter


router = APIRouter()


@router.get("/healthcheck")
async def healthcheck():
    """
        Return the API status.
    """
    return {"status": "alive"}
