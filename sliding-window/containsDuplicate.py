"""
Given an integer array nums and an integer k, return true 
if there are two distinct indices i and j in the array such 
that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
"""
from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    window = list()
    left = 0

    for right in range(len(nums)):
        validWindow = right - left
        if validWindow > k:
            window.remove(nums[left])
            left += 1
        if nums[right] in window:
            return True
        window.append(nums[right])
    return False


res = containsNearbyDuplicate([1, 0, 1, 1], 1)
print(res)