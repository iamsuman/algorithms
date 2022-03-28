class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        arr = [1] * (n+1)
        arr[0], arr[1] = 0, 0
        for i in range(2,n+1):
            j = 2
            while i * j < n+1:
                arr[i*j] = 0
                j += 1
        primes = arr.count(1)

        def fact(n):
            res = 1
            while n >1:
                res = res * n
                n -= 1
            return res

        return fact(primes) * fact(n - primes) % (10**9 + 7)


n = 5
n = 100
n = 1
s = Solution()
print(s.numPrimeArrangements(n))

