def fibonacci(n: int):

    if n in [0, 1]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":

    for i in range(10):
        print(f"{i+1}-th term of the fibonacci sequence: {fibonacci(i)}")
