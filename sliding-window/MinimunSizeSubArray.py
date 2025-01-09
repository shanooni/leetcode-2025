"""Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
 """
from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    left: int = 0
    _min: int = float('inf')
    _sum: int = 0

    if sum(nums) < target:
        return 0

    for right in range(len(nums)):
        _sum += nums[right]
        while _sum >= target:
            window = (right - left) + 1
            _min = min(_min, window)
            _sum -= nums[left]
            left += 1
    return _min


result = minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print(f"results = {result}")
