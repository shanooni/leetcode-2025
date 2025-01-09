"""
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's
anagrams
 in s. You may return the answer in any order.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

"""
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    anagramLen = len(p)
    left = 0
    results = list()

    for right in range(anagramLen, len(s) + 1):
        word = (s[left: right])
        if sorted(word) == sorted(p):
            results.append(left)
        left += 1

    return results


res = findAnagrams("abab", "ab")
print(f"res : {res}")
