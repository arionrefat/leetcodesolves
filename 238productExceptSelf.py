from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    result = 1
    counter = 1
    res = []

    for i ,j in enumerate(nums):
        result *= j
        res.append(result)
        
    print(res)
    return []


productExceptSelf([1, 2, 3, 4])  # [24,12,8,6]
