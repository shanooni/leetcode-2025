"""

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more
than once in a DNA molecule. You may return the answer in any order.


"""
from typing import List


def findRepeatedDnaSequences(s: str) -> List[str]:
    results, seen = list(), set()

    for i in range(len(s) - 9):
        print(f"index : {i}")
        print(f"seen : {seen}")
        if s[i: i + 10] in seen:
            results.append(s[i:i + 10])
            print(f"results : {results}")
        seen.add(s[i: i + 10])

    return results


print(f"ans : {findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')}")
