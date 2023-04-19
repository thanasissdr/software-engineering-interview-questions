import time
from functools import wraps


def timing(f):
    @wraps(f)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        val = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function {f.__qualname__} finished in {end-start:.4f} seconds.")

        return val

    return inner
