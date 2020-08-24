from pydantic import BaseModel

class DatabaseHealthModel(BaseModel):
    pool_minsize: int
    pool_maxsize: int
    pool_size: int
    pool_freesize: int
    closed: bool

class HealthModel(BaseModel):
    health: bool
    database: DatabaseHealthModel
