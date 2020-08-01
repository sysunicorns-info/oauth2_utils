from fastapi import APIRouter

from .realm import api_router as realm_api_router
from .realm import REALM_API_ROUTER_PREFIX

MGT_API_ROUTER_PREFIX = "/mgt"

api_router = APIRouter()
api_router.include_router(prefix=REALM_API_ROUTER_PREFIX, router=realm_api_router)
