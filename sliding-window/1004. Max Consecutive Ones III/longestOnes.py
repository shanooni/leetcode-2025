from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    zeroCount = 0
    maxLength = 0
    left = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeroCount += 1
        while zeroCount > k:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1
        maxLength = max(maxLength, right - left + 1)

    return maxLength


res = longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
print(f"res : {res}")
