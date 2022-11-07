from typing import List


def summation(list_: List) -> int | float:
    """
    Returns:
        sum of the elements of a list
    """
    s = 0

    if len(list_) == 1:
        return list_[0]

    else:
        s += list_.pop(0)
        return s + summation(list_)


if __name__ == "__main__":
    list_a = [10, 20, 30]
    print(summation(list_a))
