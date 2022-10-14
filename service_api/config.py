import logging
import os
from uuid import uuid4

from dotenv import load_dotenv

from service_api.constants import APP_NAME


load_dotenv()


class RuntimeConfig:
    APP_RUNTIME_ID = str(uuid4())
    APP_ENV = os.getenv("APP_ENV", "development")
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    PG_HOST = os.getenv("PG_HOST", "0.0.0.0")
    PG_PORT = os.getenv("PG_PORT", 5432)
    PG_NAME = os.getenv("PG_NAME", "sanic_skeleton_api")
    PG_USER = os.getenv("PG_USER", "sanic_skeleton_api")
    PG_PASSWORD = os.getenv("PG_PASSWORD", "sanic_skeleton_api")
    PG_SCHEMA = os.getenv("PG_SCHEMA", "public")
    PG_ECHO = os.getenv("PG_ECHO", True)
    UNITTEST_PG_NAME = os.getenv("UNITTEST_PG_NAME", "unittest_" + APP_NAME)

    LOG_LEVEL = logging.DEBUG
    DEBUG = True
