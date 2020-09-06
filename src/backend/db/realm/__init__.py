
import sqlalchemy


metadata = sqlalchemy.MetaData()

realm_table_metadata = sqlalchemy.Table(
    'realm', metadata,
    sqlalchemy.Column('id', sqlalchemy.String(128)),
    sqlalchemy.Column('name', sqlalchemy.String(128)),
    sqlalchemy.Column('activate', sqlalchemy.Boolean()),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime()),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime()),
    sqlalchemy.Column('is_system', sqlalchemy.Boolean())
)