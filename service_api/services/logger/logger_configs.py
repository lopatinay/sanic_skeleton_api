import logging
from service_api.config import RuntimeConfig


logger_configs = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "std_format": {
            "format": "[%(asctime)s %(name)s] [%(levelname)s] [%(module)s:%(funcName)s:%(lineno)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": logging.DEBUG,
            "formatter": "std_format",
        }
    },
    "loggers": {
        "app_logger": {
            "level": RuntimeConfig.LOG_LEVEL,
            "handlers": ["console"],
            "propagate": False
        },
    }
}
