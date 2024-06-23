from typing import List


def encode(strs: List[str]) -> str:
  result = ''

  for char in strs:
    result += str(len(char)) + '#' + char
   
  return result
        

def decode( s: str) -> List[str]:
  res, i = [], 0

  while i < len(s):
    j = i

    while s[j] != '#':
      j += 1

    length = int(s[i:j])

    res.append(s[j+1: j+ 1 + length])
    i = j + 1 + length

  return res


print(encode(["hello", "worlld"])) # "hello#world#"
print(decode("5#hello6#worlld")) # ["hello", "world"]