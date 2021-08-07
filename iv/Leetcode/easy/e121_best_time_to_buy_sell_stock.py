from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = max(prices)
        for p in prices:
            if p > min_price:
                profit = p - min_price
                if profit > max_profit:
                    max_profit = profit
            else:
                min_price = p
        return max_profit

prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
prices = [1]
s = Solution()
print(s.maxProfit(prices))


