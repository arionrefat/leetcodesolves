from typing import List


def is_valid_integer(s: str) -> bool:
    if s.startswith("-"):
        return s[1:].isdigit()
    return s.isdigit()


def calPoints(operations: List[str]) -> int:
    outputList = []

    for i in operations:
        if is_valid_integer(i):
            outputList.append(int(i))
        if i == "C":
            outputList.pop()
        if i == "D":
            outputList.append(outputList[-1] * 2)
        if i == "+":
            outputList.append(outputList[-1] + outputList[-2])

    return sum(outputList)


print(calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))

# the time complexity is O(n) and speace complexity is O(n)
# why? because we are going through the entire list and we are also creating a new list
# why the spcae complexity is O(n)? because we are creating a new list


def calPoints2(operations: List[str]) -> int:
    outputList = []

    for i in operations:
        if i == "C":
            outputList.pop()
        elif i == "D":
            outputList.append(outputList[-1] * 2)
        elif i == "+":
            outputList.append(outputList[-1] + outputList[-2])
        else:
            outputList.append(int(i))

    return sum(outputList)


print(calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
