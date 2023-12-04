from fastapi import APIRouter

management_router = APIRouter(prefix="/management")


def health_check_handler():
    return {"status": "OK"}


management_router.add_api_route(path="/health-check", endpoint=health_check_handler, methods=["GET"])
