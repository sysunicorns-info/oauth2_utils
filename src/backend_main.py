import uvicorn

from backend.application import Application
from backend.config import Config, ConfigFactory



if __name__ == "__main__":
    _config = ConfigFactory().get_config()
    uvicorn.run("backend_main:application", 
        host=_config.server_host, 
        port=_config.server_port, 
        log_level=_config.server_log_level_str
    )
else:
    application = Application()
