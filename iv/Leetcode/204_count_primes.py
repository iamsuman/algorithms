"""
Count the number of prime numbers less than a non-negative number, n.
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        sieve = [True] * n
        sieve[0] = False
        sieve[1] = False

        for i in range(2, n):
            if sieve[i]:
                for j in range(i * i, n, i):
                    sieve[j] = False
        count = 0
        i = 0
        while i < n:
            if sieve[i]:
                count = count + 1
            i += 1
        return count

A = 10
s = Solution()
print(s.countPrimes(A))



