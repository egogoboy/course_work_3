import functools
import logging
import inspect
import threading

logger = logging.getLogger("server_logger")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

thread_local = threading.local()

class MessageLogger:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        thread_local.log_buffer = []
        logger.info(f"[{self.func.__name__}]: function has been called")
        result = self.func(*args, **kwargs)

        for msg in thread_local.log_buffer:
            logger.info(f"[{self.func.__name__}]: {msg}")

        logger.info(f"[{self.func.__name__}]: function has complete work")
        return result


def consoleLog(message):
    if not hasattr(thread_local, "log_buffer"):
        thread_local.log_buffer = []
    thread_local.log_buffer.append(message)
