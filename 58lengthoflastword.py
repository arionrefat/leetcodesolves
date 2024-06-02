def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])


print(lengthOfLastWord("   fly me   to   the moon  "))

# time complexity: O(n) where n is the length of the string
# because we are splitting the string and taking the last element
# space complexity: O(n) where n is the length of the string
