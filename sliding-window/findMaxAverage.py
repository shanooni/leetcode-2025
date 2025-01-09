"""

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any
answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5],
"""
from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    sum_ = sum(nums[:k])
    maxAvg = sum_ / k
    left = 0

    for right in range(k, len(nums)):
        sum_ += nums[right]
        sum_ -= nums[left]
        avg_ = sum_ / k
        maxAvg = max(maxAvg, avg_)
        left += 1
    return maxAvg


res = findMaxAverage([5], 1)
print(f"res : {res}")
