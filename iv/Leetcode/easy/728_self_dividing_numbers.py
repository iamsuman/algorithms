class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list:
        res = []
        for i in range(left, right+1):
            if self.isselfdiv(i):
                res.append(i)
        return res

    def isselfdiv(self, num):
        n = num
        while num > 0:
            dig = num % 10
            if dig == 0 or n % dig != 0:
                return False
            num = int(num/10)
        return True


left = 1; right = 22
s = Solution()
print(s.selfDividingNumbers(left, right))
# print(s.isselfdiv(21))
