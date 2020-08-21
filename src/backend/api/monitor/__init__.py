from fastapi import APIRouter

from .health import HEALTH_API_ROUTER_PREFIX
from .health import api_router as health_api_router

MONITOR_API_ROUTER_PREFIX = "/monitor"

api_router = APIRouter()
api_router.include_router(prefix=HEALTH_API_ROUTER_PREFIX, router=health_api_router)
