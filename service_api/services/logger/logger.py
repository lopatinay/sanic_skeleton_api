import logging.config

from service_api.services.logger.logger_configs import logger_configs


logging.config.dictConfig(logger_configs)
app_logger = logging.getLogger("app_logger")
