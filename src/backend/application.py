from fastapi import FastAPI
from starlette.types import Receive, Scope, Send

from .api import api_router, API_ROUTER_PREFIX


VERSION_MAJOR=0
VERSION_MINOR=0
VERSION=f"v{VERSION_MAJOR}.{VERSION_MINOR}"

class Application(object):

    fastapi: FastAPI

    def __init__(self):
        self.fastapi = FastAPI(
            title="Backend",
            version=VERSION
        )

        self.fastapi.add_event_handler("startup", self.handle_event_startup)
        self.fastapi.add_event_handler("shutdown", self.handle_event_shutdown)

        self.fastapi.include_router(prefix=API_ROUTER_PREFIX, router=api_router)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        await self.fastapi.__call__(scope, receive, send)

    async def handle_event_startup(self):
        print("startup")

    async def handle_event_shutdown(self):
        print("shutdown")
