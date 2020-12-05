from loguru import logger
# 使用方法
# logger.debug("arg1: {}, arg2: {}", arg1, arg2)
# logger.info("That's it, beautiful and simple logging!")
# logger.warning("That's it, beautiful and simple logging!")
# logger.error("That's it, beautiful and simple logging!")
# logger.critical("That's it, beautiful and simple logging!")

# def func(a, b):
#     return a / b
# def nested(c):
#     try:
#         func(5, c)
#     except ZeroDivisionError:
#         logger.exception("What?!")
# nested(0)

logger.add(
    "../log/info/{time:YYYY-MM-DD}.log",
    format="{time:HH:MM:SS} | {level} | {name}:{line} - {message}",
    rotation="1 days",
    level="INFO")

logger.add(
    "../log/error/{time:YYYY-MM-DD}.log",
    format="{time:HH:MM:SS} | {level} | {name}:{line} - {message}",
    rotation="1 days",
    level="ERROR")