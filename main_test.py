import pytest

from main import fib


def test_fib_one() -> None:
    assert fib(1) == 1
    assert fib(0) == 1


def test_fib_other() -> None:
    assert fib(4) == 5
    assert fib(5) == 8
    assert fib(6) == 13


if __name__ == "__main__":
    pytest.main()
