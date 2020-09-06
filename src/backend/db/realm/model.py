import uuid
import sqlalchemy
import datetime

from . import realm_table_metadata

class RealmModel:

    id: uuid.UUID
    name: str
    activate: bool
    create_at: datetime.datetime
    updated_at: datetime.datetime
    is_system: bool

    def __init__(self, 
        id: uuid.uuid4,
        name: str,
        activate: bool,
        is_system: bool,
        create_at: datetime.datetime=datetime.datetime.now(),
        update_at: datetime.datetime=datetime.datetime.now()
    ):
        self.id = id
        self.activate = activate
        self.create_at = create_at
        self.updated_at = update_at
        self.is_system = is_system


    @staticmethod
    def manga_raw_to_model(realm_model_raw) -> RealmModel:
        return RealmModel(
            id=realm_model_raw[0],
            name=realm_model_raw[1],
            activate=realm_model_raw[2],
            create_at=realm_model_raw[3],
            update_at=realm_model_raw[4],
            is_system=realm_model_raw[5]
        )
