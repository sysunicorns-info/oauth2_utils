from pydantic import BaseModel
from typing import Union

class DatabaseHealthModel(BaseModel):
    health: bool
    pool_minsize: int
    pool_maxsize: int
    pool_size: int
    pool_freesize: int
    closed: bool

class HealthModel(BaseModel):
    health: bool
    database: Union[DatabaseHealthModel, None]
