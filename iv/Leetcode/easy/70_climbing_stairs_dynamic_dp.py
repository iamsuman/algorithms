class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        d[1] = 1
        d[2] = 2
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]

n = 2
n = 3
n = 45
s = Solution()
print(s.climbStairs(n))

