"""Test for main module."""

import pytest

from main import fib, is_leap_year


def test_fib_one() -> None:
    """Test for unexpected output 1."""
    assert fib(1) == 1
    assert fib(0) == 1


def test_fib_other() -> None:
    """Normal Test."""
    assert fib(4) == 5
    assert fib(5) == 8
    assert fib(6) == 13


def test_fib_neg() -> None:
    """Erroneous Test."""
    with pytest.raises(ValueError, match="-1"):
        fib(-1)


def test_not_leap_year() -> None:
    """Test for invalid leap year."""
    assert is_leap_year(2013) is False
    assert is_leap_year(2014) is False


def test_is_leap_year() -> None:
    """Test for valid leap year."""
    assert is_leap_year(2012) is True
    assert is_leap_year(2016) is True


def test_centennial_year() -> None:
    """Test for invalid centennial year."""
    assert is_leap_year(1900) is False
    assert is_leap_year(1800) is False


def test_four_hundred() -> None:
    """Test for valid leap year every four hundred year."""
    assert is_leap_year(2000) is True
    assert is_leap_year(1600) is True
