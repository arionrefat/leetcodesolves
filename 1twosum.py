from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    indices = []

    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if i != j and (nums[i] + nums[j]) == target:
                indices.append(i)
                indices.append(j)

    return indices


print(twoSum([2, 7, 11, 15], 9))


# here this time complexity is O(n^2) and space complexity is O(1)
# this is a brute force approach
