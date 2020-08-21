import uvicorn

from backend.application import Application

application = Application()

if __name__ == "__main__":
    uvicorn.run("backend_main:application", host="127.0.0.1", port=5000, log_level="debug")
