from fastapi import APIRouter

api_router = APIRouter()

REALM_API_ROUTER_PREFIX = "/realm"

@api_router.get(
    path="/", 
    tags=["management/realm"],
    summary="Get Realm List",
    description="Get Realm List"
)
async def get_realm_list():
    pass

@api_router.get(
    path="/{realm_id}", 
    tags=["management/realm"],
    summary="Get Realm Details Information",
    description="Get Realm Details Information"
)
async def get_realm_detail(realm_id: str):
    pass

@api_router.post(
    path="/", 
    tags=["management/realm"],
    summary="Add Realm",
    description="Add Realm"
)
async def add_realm():
    pass

@api_router.delete(
    path="/{realm_id}", 
    tags=["management/realm"],
    summary="Delete Realm",
    description="Delete Realm and all attached resources"
)
async def del_realm(realm_id: str):
    pass

@api_router.post(
    path="/{realm_id}", 
    tags=["management/realm"],
    summary="Update Realm Information",
    description="Update Realm Information"
)
async def update_realm(realm_id: str):
    pass
