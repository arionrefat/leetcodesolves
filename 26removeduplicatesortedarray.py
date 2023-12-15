from typing import List


def removeDuplicates(nums: List[int]) -> int:
    nums[:] = sorted(list(set(nums)))

    return len(set(nums))


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

"""
Time Complexity: O(n)
Space Complexity: O(1)

nums =  doesn't replace elements in the original list.
nums[:] = replaces element in place

In short, without [:], we're creating a new list object, which is against what this problem is asking for:
"Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory."
"""
