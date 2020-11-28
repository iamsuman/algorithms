import math

class Solution():
    def isUgly(self, num: int):
        if not num:
            return False
        if num <= 0:
            return False

        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        return not num - 1

    def isUgly3(self, num: int):
        # Time limit exceeded
        if num <= 0:
            return False
        if num in [1, 2, 3, 5]:
            return True

        ugly_factors = [2, 3, 5]
        res = False

        i = 2
        maxi = int(num / 2 + 1)
        while i < maxi:
            if num == 1:
                break
            if num % i == 0:
                if i in ugly_factors:
                    res = True
                else:
                    return False
                num = int(num / i )
            else:
                i = i + 1
        return res




    def isUgly2(self, num: int):
        # Time Limit exceeded
        if num <= 0:
            return False
        if num in [1, 2, 3, 5]:
            return True

        sieve = [0] * (int(num / 2) + 1)
        sieve[0] = 1
        sieve[1] = 1
        for i in range(2, int(num / 2) + 1):
            if sieve[i] != 0:
                continue
            for j in range(i * i, int(num / 2) + 1, i):
                sieve[j] = 1
        # print(sieve)

        res = False
        ugly_factors = [2, 3, 5]
        for i in range(2, int(num / 2) + 1):
            if sieve[i] == 1:
                continue
            if num % i == 0:
                if i not in ugly_factors:
                    return False
                else:
                    res = True
        return res

num = 100
num = 6
num = 14
s = Solution()
print(s.isUgly(num))



