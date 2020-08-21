from fastapi import FastAPI
from starlette.types import Receive, Scope, Send

from .api import api_router, API_ROUTER_PREFIX
from .db import Database
from .config import Config

VERSION_MAJOR=0
VERSION_MINOR=0
VERSION=f"v{VERSION_MAJOR}.{VERSION_MINOR}"
NAME="OAuth2 - Backend"

class Application(FastAPI):

    database: Database = None
    config: Config = None
    fastapi: FastAPI = None

    def __init__(self):
        self.config = Config(
            db_host="127.0.0.1",
            db_user="oauth2",
            db_pwd="oauth2",
            db_name="oauth2"
        )

        self.database = Database(
            dsn=Database.dsn(
                host=self.config.db_host,
                user=self.config.db_user,
                pwd=self.config.db_pwd,
                name=self.config.db_name
            ), 
            application_name=NAME
        )

        self.fastapi = FastAPI(
            title=NAME,
            version=VERSION
        )

        self.fastapi.add_event_handler("startup", self.handle_event_startup)
        self.fastapi.add_event_handler("shutdown", self.handle_event_shutdown)

        self.fastapi.include_router(prefix=API_ROUTER_PREFIX, router=api_router)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        return await self.fastapi.__call__(scope=scope, receive=receive, send=send)

    async def handle_event_startup(self):
        print("startup")
        await self.database.init_pool();

    async def handle_event_shutdown(self):
        print("shutdown")
        await self.database.close_pool();
