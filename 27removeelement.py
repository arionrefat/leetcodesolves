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


# the time complexity is O(n) and space complexity is O(1)
# is there any wayt to imrpove the time complexity?
# we can use two pointers
# one pointer to iterate the array and another pointer to place the elements
# the time complexity is O(n) and space complexity is O(1)
