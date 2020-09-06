from .model import RealmModel
from backend.db import Database


class RealmRepository:

    database: Database = None

    def __init__(self, database: Database):
        self.database = database
