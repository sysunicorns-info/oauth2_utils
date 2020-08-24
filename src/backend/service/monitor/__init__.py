from backend.db import Database

class MonitorService():

    database: Database

    def __init__(self, database: Database):
        self.database = database

    async def get_health(self):
        """
        """
        
        return {
            'health': True,
            'database': {
                'pool_minsize': self.database.engine.minsize,
                'pool_maxsize': self.database.engine.maxsize,
                'pool_size': self.database.engine.size,
                'pool_freesize': self.database.engine.freesize,
                'closed': self.database.engine.closed,
            }
        }
