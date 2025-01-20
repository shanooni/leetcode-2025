def maxVowels(s: str, k: int) -> int:
    vowels = {'u', 'i', 'o', 'e', 'a'}
    currentVowelCount = 0
    maxVowelCount = 0

    for i in range(k):
        if s[i] in vowels:
            currentVowelCount += 1
        maxVowelCount = currentVowelCount
    for j in range(k, len(s)):
        if s[j] in vowels:
            currentVowelCount += 1
        if s[j - k] in vowels:
            currentVowelCount -= 1
        maxVowelCount = max(maxVowelCount, currentVowelCount)

    return maxVowelCount


print(maxVowels("leetcode", 3))
