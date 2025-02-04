from typing import List


def removeElement(nums: List[int], val: int) -> int:
    slowPtr: int = 0

    for fastPtr in range(len(nums)):
        print(f"nums : {nums}")
        if nums[fastPtr] != val:
            nums[slowPtr] = nums[fastPtr]
            slowPtr += 1
    return slowPtr


removeElement([3, 2, 2, 3], 3)
