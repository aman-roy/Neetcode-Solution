from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        max_profit = 0
        for price in prices:
            smallest = min(smallest, price)
            max_profit = max(max_profit, abs(smallest-price))
        return max_profit

assert (Solution().maxProfit([7,1,5,3,6,4])) == 5
assert (Solution().maxProfit([7,6,4,3,1])) == 0
