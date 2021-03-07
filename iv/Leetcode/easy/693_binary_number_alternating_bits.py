class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n <= 1:
            return False
        res = ""
        prev = None
        while n > 0:
            new = str(n % 2)
            if prev is not None:
                if prev == new:
                    return False
            prev = new
            res = str(n % 2) + res
            n = int(n / 2)
        # print(res)
        return True

n = 5
# n = 7
n = 11
n = 10
s = Solution()
print(s.hasAlternatingBits(n))


