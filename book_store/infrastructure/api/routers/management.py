from fastapi import APIRouter

management_router = APIRouter(prefix="/management", tags=["Management"])


@management_router.get("/health-check", status_code=200)
def health_check_handler():
    return {"status": "OK"}
