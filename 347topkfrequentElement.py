from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    result = []
    freq = [[] for i in range(len(nums)+ 1)]

    # here we are counting the frequency of each element
    for i in nums:
        count[i] = 1 + count.get(i,0)

    print(count.items())

    # here we are storing the frequency of each element
    for n, c in count.items():
        freq[c].append(n)

    # here we are storing the result
    for i in range(len(freq) - 1, 0 , -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result
            

topKFrequent([1,1,1,2,2,3], 2) # [1,2]