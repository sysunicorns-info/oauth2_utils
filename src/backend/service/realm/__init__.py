from backend.db import Database
import random

class RealmService():

    database: Database = None

    def __init__(self, database: Database):
        self.database = database

    def create_realm(self):
        pass

    def update_realm(self):
        pass

    def delete_realm(self):
        pass

    def get_realm_list(self):
        pass

    def get_realm_by_name(self):
        pass

    def get_realm_by_id(self):
        pass
