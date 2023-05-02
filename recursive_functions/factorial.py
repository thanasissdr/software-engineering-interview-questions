from typing import Dict, List

from benchmark import timing


@timing
def factorial_recursive_memoization(n: int, memo: Dict[int, int] = None) -> int:
    """
    Recursive implementation of factorial
    with memoization
    """
    if memo is None:
        memo = {}

    if n in [0, 1]:
        return 1

    if n in memo:
        return memo[n]

    result = n * factorial_recursive_memoization(n - 1, memo)
    memo[n] = result
    return result


@timing
def factorial_cached(n: int) -> int:
    """
    Factorial implementation
    with caching
    """
    i = 1

    cached = {}
    cached[1] = 1
    cached[0] = 1

    while i <= n:
        cached[i] = cached[i - 1] * i
        i += 1

    return cached[n]


@timing
def factorial_optimized(n: int) -> int:
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p


def main(n: int) -> None:
    for f in [
        factorial_recursive_memoization,
        factorial_cached,
        factorial_optimized,
    ]:
        print(f(n))


if __name__ == "__main__":
    n = 4
    print(main(n))
