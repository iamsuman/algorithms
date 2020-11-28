class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (left + right) // 2
            summ = (k * (k + 1))/ 2
            if summ == n:
                return k
            if summ > n:
                right = k - 1
            else:
                left = k + 1
        return right

    def arrangeCoins2(self, n: int) -> int:
        if n == 0:
            return 0
        summ = 0
        for i in range(1,n + 1):
            summ += i
            if summ > n:
                return i - 1
            elif summ == n:
                return i


n = 5
n = 8
# n = 1
s = Solution()
print(s.arrangeCoins(n))

# i = 1, 2, 3
# summ = 1, 3, 6


