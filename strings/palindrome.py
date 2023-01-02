import time
from functools import wraps


def timing(f):
    @wraps(f)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        val = f(*args, **kwargs)
        end = time.perf_counter()

        print(f"Function {f.__qualname__} finished in {end - start:.2f} seconds.")

        return val

    return inner


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def is_palindrome_2(s: str) -> bool:
    l = len(s)
    i = 0

    if l % 2 == 1:
        while i < (l // 2):
            if s[i] != s[l - i - 1]:
                return False
            i += 1
    else:

        while i < (l / 2):
            if s[i] != s[l - i - 1]:
                return False

            i += 1

    return True


if __name__ == "__main__":
    strings = ["abba", "abc"]
    for s in strings:
        if is_palindrome(s):
            print(f"{s} is palindrome")
        else:
            print(f"{s} is not palindrome")
