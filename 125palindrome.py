def isPalindrome(s: str) -> bool:
    newString = ""

    for n in s:
        if n.isalnum():
            newString += n.lower()
    return newString == newString[::-1]


# here the time complexity is O(n) and space complexity is O(n)
# as we are storing the new string in the newString variable
print(isPalindrome("A man, a plan, a canal: Panama"))


# Another way
def isAlphanumeric(c: str) -> bool:
    return (
        (ord("A") <= ord(c) <= ord("Z"))
        or (ord("a") <= ord(c) <= ord("z"))
        or (ord("0") <= ord(c) <= ord("9"))
    )


def palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not isAlphanumeric(s[left]):
            left += 1
        while right > left and not isAlphanumeric(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left, right = left + 1, right - 1
    return True


print(palindrome("A man, a plan, a canal: Panama"))
