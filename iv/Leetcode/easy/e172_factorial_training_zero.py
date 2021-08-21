class Solution:
    def trailingZeroes(self, n: int) -> int:
        l2 = [self.func(i, 2) for i in range(1, n+1) if i % 2 == 0]
        l5 = [self.func(i, 5) for i in range(1, n + 1) if i % 5 == 0]
        suml2 = sum(l2)
        suml5 = sum(l5)
        r = min(suml2, suml5)
        return r

    def func(self, n, i):
        count = 0
        while n > 0:
            if n % i == 0:
                count += 1
                n = n // i
            else:
                break
        return count



    def trailingZeroes2(self, n: int) -> int:
        fact = self.factorial(n)
        count = 0
        while fact > 0:
            if fact % 10 == 0:
                count += 1
                fact = fact // 10
            else:
                break
        return count

    def factorial(self, n: int):
        if n == 0:
            return 1
        res = 1
        while n > 0:
            res = res * n
            n -= 1
        return res


n = 3
n = 5
n = 0
n = 10
n = 8785
s = Solution()
print(s.trailingZeroes(n))
# print(s.factorial2(n))
print(s.trailingZeroes2(n))




