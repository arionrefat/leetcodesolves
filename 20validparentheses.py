def isValid(s: str) -> bool:
    listofparenthesis = list(s)
    matched = False

    for _ in range(len(listofparenthesis) - 1):
        lastindex = listofparenthesis.pop()
        if len(listofparenthesis) != 0 and s[0] == lastindex:
            matched = True
        else:
            matched = False

    return matched


print(isValid("{}[]"))
