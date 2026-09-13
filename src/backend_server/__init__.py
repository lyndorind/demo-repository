import uvicorn
from opentelemetry.instrumentation.auto_instrumentation import initialize

from .logging import log_config
from .main import app

__version__ = "0.0.1"

def main():
    initialize()
    uvicorn.run("backend_server:app", host="0.0.0.0", port=8000, workers=1, log_config=log_config)
