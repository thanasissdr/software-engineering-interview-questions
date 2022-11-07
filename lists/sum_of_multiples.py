from typing import List


def get_sum_of_multiples(list_: List, *args):
    """
    Returns the sum of all elements in the list_ if they are multiples
    of any of the elements that are in args.
    """
    return sum(i for i in list_ if any(i % arg == 0 for arg in args))


if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(get_sum_of_multiples(list_, 3, 5))
    # 3 + 5 + 6 + 9 + 10 = 33
