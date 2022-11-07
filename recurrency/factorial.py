def factorial(n: int):

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":

    for i in range(10):
        print(f"factorial of {i}: {factorial(i)}")
