class Solution:
    def fizzBuzz(self, n: int) -> list:
        sieve = [0] * (n + 1)
        for i in (3, 5):
            for j in range(i, n+1, i):
                sieve[j] += i

        res = []
        for i in range(1, n+1):
            if sieve[i] == 0:
                res.append(str(i))
            elif sieve[i] == 3:
                res.append("Fizz")
            elif sieve[i] == 5:
                res.append("Buzz")
            else:
                res.append("FizzBuzz")
        return res

n = 15
s = Solution()
print(s.fizzBuzz(n))


