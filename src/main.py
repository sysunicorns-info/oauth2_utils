import uvicorn

from backend.application import Application
from backend.config import Config, ConfigFactory



if __name__ == "__main__":
    _config = ConfigFactory().get_config()
    uvicorn.run("main:application", 
        host=_config.server_host, 
        port=_config.server_port, 
        log_level=_config.server_log_level,
        log_config=_config.server_log_config
    )
else:
    application = Application()
