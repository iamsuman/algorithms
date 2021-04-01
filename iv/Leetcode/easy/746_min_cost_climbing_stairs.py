class Solution:
    def minCostClimbingStairs(self, cost: list) -> int:
        n = len(cost)
        res = [0] * n
        if n <= 2:
            return min(cost)

        res[0] = cost[0]
        res[1] = cost[1]
        for i in range(2, n):
            res[i] = min(res[i-1], res[i-2]) + cost[i]
        # print(res)
        return min(res[n-1], res[n-2])


cost = [10, 15, 20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
s = Solution()
print(s.minCostClimbingStairs(cost))




