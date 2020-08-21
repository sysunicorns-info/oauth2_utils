from fastapi import APIRouter, Depends

api_router = APIRouter()

HEALTH_API_ROUTER_PREFIX = ""

@api_router.get(path="/health")
async def get_health():
    return "{}"
