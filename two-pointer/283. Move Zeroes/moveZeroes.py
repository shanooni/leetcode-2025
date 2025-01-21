from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # start = 0
    # end = len(nums)
    # zeroCount = 0
    # ans = []
    # while start < end:
    #     if nums[start] == 0:
    #         zeroCount += 1
    #     if nums[start] != 0:
    #         ans.append(nums[start])
    #     start += 1
    # zeros = [0] * zeroCount
    # ans = ans + zeros
    slow_ptr = 0
    for fast_ptr in range(len(nums)):
        if nums[fast_ptr] != 0:
            nums[slow_ptr] = nums[fast_ptr]
            slow_ptr += 1
    for i in range(slow_ptr, len(nums)):
        nums[i] = 0
    print(f"nums : {nums}")


moveZeroes([0, 1, 0, 3, 12])
# moveZeroes([0])
