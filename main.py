def fib(n):
    if n == 1:
        x = 1
    elif n == 0:
        x = 1
    else:
        x = fib(n - 1) + fib(n - 2)
    return x


# print(fib(int(input("Number in sequence: "))))
