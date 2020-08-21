from backend.db import Database
import random

class RealmService():

    database: Database = None
    index: int = 0

    def __init__(self):
        self.index = random.randint(0, 10)
