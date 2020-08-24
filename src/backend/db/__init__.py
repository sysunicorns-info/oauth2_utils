import aiopg
from aiopg.sa import create_engine, Engine
import asyncio
from contextlib import AbstractAsyncContextManager

class Database():

    engine: Engine = None

    _dns: str
    _application_name: str
    _pool_minsize: int
    _pool_maxsize: int

    def __init__(self, 
            dsn: str, application_name: str, 
            pool_minsize: int =10, pool_maxsize: int =20
        ):
        self._dns = dsn
        self._application_name = application_name
        self._pool_minsize = pool_minsize
        self._pool_maxsize = pool_maxsize

    @staticmethod
    def dsn(host: str, user: str, pwd: str, name: str):
        return f"dbname={name} user={user} password={pwd} host={host}"

    async def init_pool(self):
        print('init')
        self.engine = await create_engine(
            dsn=self._dns, 
            minsize=self._pool_minsize, maxsize=self._pool_maxsize
        )

    async def acquire(self):
        return await self.engine.acquire()

    async def close_pool(self):
        print('close')
        self.engine.close()
        await self.engine.wait_closed()
        del self.engine

    def __del__(self):
        print("db del")
