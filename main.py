"""Calculate the nth Fibonacci number."""

from typing import Any, TypedDict, Literal


class Details(TypedDict):
    """The details of a player."""

    name: str
    score: int
    colour: tuple[int, int, int]
    items: list[dict[str, Any]]


details: Details = {"name": "Matthew", "score": 70, "colour": (255, 75, 0), "items": []}


class Shark(TypedDict):
    """The Shark class."""

    name: str
    species: Literal["Reef Shark", "Nurse Shark"]
    age: int
    weight: float
    dimensions: tuple[int, float, float]
    vaccinated: bool


A: Shark = {
    "name": "Billy",
    "species": "Reef Shark",
    "age": 5,
    "weight": 700,
    "dimensions": (565, 70.8, 54.3),
    "vaccinated": False,
}

B: Shark = {
    "name": "Milo",
    "species": "Nurse Shark",
    "age": 8,
    "weight": 940,
    "dimensions": (829, 96.0, 47.8),
    "vaccinated": True,
}


def fib(n: int) -> int:
    """Calculates the nth Fibonacci number.

    Args:
        n (int): The number to calculate the fibonacci number.


    Returns:
        int: The nth Fibonacci number.


    Raises:
        ValueError: If n is negative.
    """
    if n == -1:
        raise ValueError("-1")
    return 1 if n in [1, 0] else fib(n - 1) + fib(n - 2)



def is_leap_year(year: int) -> bool:
    """Checks whether the given year is a leap year.

    Args:
        year (int): The year to check.


    Returns:
        bool: Whether the given year is a leap year.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return year % 400 == 0
            return False
        return True
    return False
