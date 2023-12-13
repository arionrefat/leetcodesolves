from typing import List


def removeElement(nums: List[int], val: int) -> int:
    counter = 0

    orginalLength = len(nums)

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.remove(val)
            counter += 1
    return orginalLength - counter


print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
