def isPalindrome(s: str) -> bool:
    newString = s.replace(" ", "").replace(",", "").replace(":", "").lower()
    start: int = 0
    end: int = len(newString) - 1
    while start <= end:
        if newString[start].isalnum() != newString[end].isalnum():
            return False
        start += 1
        end -= 1
    return True


res = isPalindrome("race a car")
print(f"ans : {res}")
