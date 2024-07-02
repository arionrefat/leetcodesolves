from typing import List


def maxProfit(prices: List[int]) -> int:
    l, r = 0, 1
    maxp = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxp = max(maxp, profit)
        else:
            l = r
        r += 1
    return prices

# the time complexity is O(n) because we only iterate through the list once
# the space complexity is O(1) because we only use a few variables