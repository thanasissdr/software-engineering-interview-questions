def get_n_term(start: int, steps: int, common_difference: int) -> int:
    return start + steps * common_difference


def sum_arithmetic_progression(start: int, steps: int, common_difference: int) -> int:
    end = get_n_term(start, steps, common_difference)
    n = steps + 1

    summa = (n / 2) * (start + end)
    return int(summa)


def summation_of_up_and_down(
    start: int, steps_up: int, steps_down: int, common_difference: int = -1
) -> int:
    sum_upwards = sum_arithmetic_progression(start, steps_up, common_difference)
    top = get_n_term(start, steps_up, common_difference)
    sum_downwards = (
        sum_arithmetic_progression(top, steps_down, -common_difference) - top
    )

    return sum_upwards + sum_downwards


if __name__ == "__main__":
    print(
        summation_of_up_and_down(start=1, steps_up=3, steps_down=4, common_difference=2)
    )
