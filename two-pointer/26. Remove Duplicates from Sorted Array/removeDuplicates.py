from typing import List


def removeDuplicates(nums: List[int]) -> int:
    # numberDuplicate = 1
    # left = 0
    # right = 1
    #
    # while right < len(nums):
    #     if nums[left] != nums[right]:
    #         numberDuplicate += 1
    #         left = right
    #     right += 1
    #     print(f"nums : {nums}")
    # return numberDuplicate
    j: int = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    print(f"nums : {nums}")
    return j


res = removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(f"res : {res}")
