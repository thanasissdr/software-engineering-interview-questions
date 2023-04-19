from typing import List

from benchmark import timing


def factorial(n: int) -> int:
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_cached(n: int) -> int:
    """
    Theoretically this should be faster,
    since it uses caching, rather than calculating
    factorials from scratch.
    """
    i = 1

    cached = {}
    cached[1] = 1
    cached[0] = 1

    while i <= n:
        cached[i] = cached[i - 1] * i
        i += 1

    return cached[n - 1] * n


@timing
def main(arr):
    for i in arr:
        print(factorial(i))


if __name__ == "__main__":
    arr = [1001]
    print(main(arr))
