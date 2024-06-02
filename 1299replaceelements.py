from typing import List


def replaceElements0(arr: List[int]) -> List[int]:
    result = []

    for i in range(len(arr)):
        if i == len(arr) - 1:
            result.append(-1)
        else:
            result.append(sorted(arr[i + 1 : :], reverse=True)[0])

    return result


# replaceElements([17, 18, 5, 4, 6, 1])
# brute force solution
# time complexity: O(n^2) because of the sorting added in the loop
# for each iteration of the array
# space complexity: O(n) because of the result array


def replaceElements(arr: List[int]) -> List[int]:
    right_max = -1

    for i in range(len(arr) - 1, -1, -1):
        newMax = max(right_max, arr[i])
        arr[i] = right_max
        right_max = newMax

    return arr


# time complexity O(n) because of the loop
# space complexity O(1) because we are modifying the input array
# and not creating a new one
