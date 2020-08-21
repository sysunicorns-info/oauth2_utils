from dataclasses import dataclass

@dataclass
class Config():
    db_host: str
    db_user: str
    db_pwd: str
    db_name: str
