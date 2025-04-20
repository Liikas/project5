import pytest
from src.decorators import log
import os


def test_log_success(capsys):
    @log()
    def test_func():
        return 42

    test_func()
    captured = capsys.readouterr()
    assert "test_func ok" in captured.out


def test_log_file():
    @log(filename="test_log.txt")
    def test_func():
        return 42

    test_func()
    with open("test_log.txt", "r") as f:
        content = f.read()
    assert "test_func ok" in content
    os.remove("test_log.txt")
