from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)  # mapping charCount to a list of anagrams

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        result[tuple(count)].append(s)

    return result.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# the time complexity for the above code is O(n * m) where n is the number of
# strings in the input list and m is the maximum length of a string in the list.
# for each string, we iterate over each character to calculate the count array.
# the space complexity is O(n * m) as well.
