from fastapi import APIRouter

from .management import api_router as mgt_api_router
from .management import MGT_API_ROUTER_PREFIX

from .monitor import api_router as monitor_api_router
from .monitor import MONITOR_API_ROUTER_PREFIX

API_ROUTER_PREFIX = "/api"

api_router = APIRouter()
api_router.include_router(prefix=MGT_API_ROUTER_PREFIX, router=mgt_api_router)
api_router.include_router(prefix=MONITOR_API_ROUTER_PREFIX, router=monitor_api_router)
