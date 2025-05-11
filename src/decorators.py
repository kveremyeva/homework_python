import logging
from functools import wraps
from typing import Any, Callable, Optional

logging.basicConfig(filename=r'E:\Python\PythonProject3\tests\mylog.txt', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
#logging.basicConfig(filename=r'E:\Python\PythonProject3\tests\mylog.txt', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def log(filename: Optional[str] = None) -> Callable[[Callable[..., str]], Callable[..., str]]:
    """Декоратор для логирования вызовов функций."""
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> str:
            logging.info(f"Starting the function '{func.__name__}' with arguments: {args}, {kwargs}")
            try:
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__} ok")
                return result
            except Exception as exc:
                logging.error(
                    f"{func.__name__} error: {type(exc).__name__}. Inputs: {args}, {kwargs}")
                raise
        return inner
    return decorator


@log()
def my_function(x: Any, y: Any) -> Any:
    """Сложение двух чисел"""
    return x + y


my_function(1, 2)
