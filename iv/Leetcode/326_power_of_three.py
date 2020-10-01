class Solution:
    def isPowerOfThree(self, n: int):
        if n == 0:
            return False
        while n % 3 == 0:
            n = int(n / 3)
        if n == 1:
            return True
        else:
            return False


n = 27
n = 0
s = Solution()
print(s.isPowerOfThree(n))




