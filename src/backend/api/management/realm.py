from fastapi import APIRouter

api_router = APIRouter()

REALM_API_ROUTER_PREFIX = "/realm"

@api_router.get(path="/")
async def get_realm_list():
    pass

@api_router.get(path="/{realm_id}")
async def get_realm_detail(realm_id: str):
    pass

@api_router.post(path="/")
async def add_realm():
    pass

@api_router.delete(path="/{realm_id}")
async def del_realm(realm_id: str):
    pass

@api_router.post(path="/{realm_id}")
async def update_realm(realm_id: str):
    pass
