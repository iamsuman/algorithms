from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max(prices)
        max_price = 0
        profit = 0
        total_profit = 0
        for p in prices:
            if p > min_price:
                if p > max_price:
                    max_price = p
                    profit = p - min_price
                elif p < max_price:
                    max_price = 0
                    min_price = p
                    total_profit += profit
                    profit = 0
            elif p <= min_price:
                if p < max_price:
                    max_price = 0
                    min_price = p
                    total_profit += profit
                    profit = 0
                min_price = p
        if profit != 0:
            total_profit += profit
        return total_profit


prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
prices = [7,1,5,3,6,3,8]
# prices = [1,2,4,2,5,7,2,4,9,0]
s = Solution()
print(s.maxProfit(prices))


