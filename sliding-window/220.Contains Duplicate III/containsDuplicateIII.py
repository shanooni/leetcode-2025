from typing import List


def containsNearbyAlmostDuplicate(nums: List[int], indexDiff: int, valueDiff: int) -> bool:
    # this set  keeps track of all element within the valid window
    window = set()
    left = 0

    for right in range(len(nums)):
        validWindow = right - left
        if validWindow > indexDiff:
            window.remove(nums[left])
            left += 1
        print(f"left != right : {left != right}")
        print(f"abs(left - right) : {abs(left - right)} : indexDiff {indexDiff} : abs(left - right) <= indexDiff {abs(left - right) <= indexDiff} ")
        print(f"abs(nums[right] - nums[left]) : {abs(nums[right] - nums[left])} : valueDiff {valueDiff} : abs(nums["
              f"right] - nums[left]) <= valueDiff {abs(nums[right] - nums[left]) <= valueDiff}")
        if left != right and abs(left - right) <= indexDiff and abs(nums[right] - nums[left]) <= valueDiff:
            return True
        window.add(nums[right])
    return False


res = containsNearbyAlmostDuplicate([1, 2, 2, 3, 4, 5], 3, 0)  # expect true
# res = containsNearbyAlmostDuplicate([8, 7, 15, 1, 6, 1, 9, 15], 1, 3) # expect true
print(res)
