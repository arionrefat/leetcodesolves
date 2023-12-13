from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()

    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False


# The time complexity of this approach is O(n), where n is the length of the array.
# the space complexity is O(n) as well, where n is the length of the array.
