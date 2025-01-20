from typing import List


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    res = []
    for i in range(k):
        res.append(arr[i])

    for j in range(k, len(arr) - 1):
        res.append(arr[j])
        if abs(arr[j] - x) < abs(arr[j + 1] - x) or abs(arr[j] - x) == abs(arr[i + 1] - x) and i < j + 1:
            res.remove(arr[k - j])
    return res


print(findClosestElements([1, 1, 2, 3, 4, 5], 4, -1))
