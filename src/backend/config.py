from dataclasses import dataclass

@dataclass
class Config():
    application_name: str
    server_host: str
    server_port: int
    server_log_level_str: str
    db_host: str
    db_user: str
    db_pwd: str
    db_name: str
    origins: list()

class ConfigFactory():

    config: Config

    def __init__(self):
        self.config = Config(
            application_name="OAuth2 - Backend",
            server_host="127.0.0.1",
            server_port=5000,
            server_log_level_str="debug",
            db_host="127.0.0.1",
            db_user="oauth2",
            db_pwd="oauth2",
            db_name="oauth2",
            origins = [
                "http://localhost:5000",
            ]
        )

    def get_config(self) -> Config:
        return self.config
