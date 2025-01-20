from typing import List


def findLength(nums1: List[int], nums2: List[int]) -> int:
    """
    get sub array for each of the list
    :param nums1:
    :param nums2:
    :return:
    """
    left = 1
    sub1 = list()
    for right in range(len(nums1)):
        sub1.append(nums1[right:])
        sub1.append(nums1[:right+1])
        left += 1
    sub2 = list()
    for right in range(len(nums2)):
        sub2.append(nums2[right:])
        sub2.append(nums2[:right + 1])
    print(f"sub1 : {sub1}")
    print(f"sub2 : {sub2}")
    res = list()
    for sub in sub1:
        if sub in sub2:
            res.append(sub)
    print(f"res : {res}")
    return 0


findLength([0, 1, 1, 1, 0], [1, 1, 1, 1, 1])
