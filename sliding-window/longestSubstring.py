"""
Given a string s, find the length of the longest 
substring
without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


def lengthOfLongestSubstring(s: str) -> int:
    _set: set = set()
    longest: int = 0
    left: int = 0

    for right in range(len(s)):
        while s[right] in _set:
            _set.remove(s[left])
            left += 1
        _set.add(s[right])
        window = (right - left) + 1
        longest = max(longest, window)

    return longest


results = lengthOfLongestSubstring("abcabcbb")
print(f"results : {results}")
