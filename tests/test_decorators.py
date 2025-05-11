import pytest
import logging
from src.decorators import log, my_function


def test_log_decorator(capsys):
    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
         return x + y

    my_function(1, 2)
    with open("mylog.txt") as f:
         log_content = f.read()
         assert 'my_function ok' in log_content


def test_decorator_empty(capsys):
    @log(filename="mylog.txt")
    def test_empty():
        with pytest.raises(TypeError):
            my_function()
        capture = capsys.readouterr()
        assert capture



def test_log_error(capsys):
    @log(filename="mylog.txt")
    def test_func(x, y):
        with pytest.raises(TypeError):
            my_function("1, 2")
        capture = capsys.readouterr()
        assert capture



def test_file_logging_error() -> None:
    @log(filename="mylog.txt")
    def error_func(x) -> None:
        raise ValueError(f"Неверное значение: {x}")

    with pytest.raises(ValueError):
        error_func(1)

    with open("mylog.txt") as f:
        log_content = f.read()
        assert  "my_function error: TypeError. Inputs: (1,), {}" in log_content
