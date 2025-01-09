from typing import List


def findLHS(nums: List[int]) -> int:
    """
    loop through the numbers of numbers and insert in a dictionary.
    the key is the number
    the value is the count
    get the min, and the max values from the dictionary and sum the up
    :param nums:
    :return: return the greatest max sum
    """
    map_ = {}
    max_ = 0

    if len(set(nums)) == 1:
        return 0

    for num in range(len(nums)):
        map_[nums[num]] = map_.get(nums[num], 0) + 1

    for i in range(len(nums)):
        min_ = nums[i]
        max__ = min_ + 1
        res_ = map_.get(min_, 0) + map_.get(max__, 0)
        max_ = max(res_, max_)
    return max_


res = findLHS([1, 3, 2, 2, 5, 2, 3, 7])
print(f"res : {res}")
