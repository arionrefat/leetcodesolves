from typing import List


def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        # we are checking if n-1 is present in the set or not, 
        # if it is not present then we can start counting from n
        if (n - 1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest


# here the time complexity is O(n) and space complexity is O(n) as we are using a set to store the elements of the array
