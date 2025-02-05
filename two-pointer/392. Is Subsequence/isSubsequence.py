def isSubsequence(s: str, t: str) -> bool:
    left = 0
    res = []
    for right in range(len(t)):
        if t[right] == s[left]:
            res.append(True)
            left += 1
    return len(res) == len(s)
# Need to be optimised for some edge cases
