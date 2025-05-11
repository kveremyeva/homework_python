import pytest

from src.decorators import log, my_function


@log(filename="mylog.txt")
def test_log_decorator(capsys):
    def summ(x: int, y: int) -> int:
        return x + y

    print(summ(1, 2))
    capture = capsys.readouterr()
    assert capture


@log(filename="mylog.txt")
def test_decorator_empty(capsys):
    with pytest.raises(TypeError):
        my_function()
    capture = capsys.readouterr()
    assert capture


@log(filename="mylog.txt")
def test_decorator_text(capsys):
    with pytest.raises(TypeError):
        my_function("1, 2")
    capture = capsys.readouterr()
    assert capture
