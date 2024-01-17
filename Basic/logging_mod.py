from logging import *

LOG_FORMAT = "{lineno} || {name} || {asctime} || {message}"

basicConfig(filename="log_file.log", level=DEBUG, filemode="w", format=LOG_FORMAT, style="{")


# #!      1 - Example
# debug("Debug")
# info("Info")
# warning("Warning")
# error("Error")
# critical("Critical")


#!      2 - Example
logger = getLogger("king")

logger.debug("Debug")
logger.info("Info")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")