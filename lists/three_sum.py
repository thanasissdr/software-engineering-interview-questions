from typing import List


def three_sum(nums: List) -> List:
    """
    Return all the triplets in nums such that their sum is zero
    without any replacement.
    """
    res = []

    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                summa = nums[i] + nums[j] + nums[k]
                if summa == 0:
                    sol = [nums[i], nums[j], nums[k]]
                    res.append(sol)
    return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, 4]
    print(three_sum(nums))
