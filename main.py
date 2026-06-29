def fib(n: int) -> int:
    return 1 if n in [1, 0] else fib(n - 1) + fib(n - 2)
