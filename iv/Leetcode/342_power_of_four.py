class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        if (num & (num - 1) == 0) and ((num - 1) % 3 == 0):
            return True
        else:
            return False

    def isPowerOfFour2(self, num: int) -> bool:
        if num < 1:
            return False
        while num % 4 == 0:
            num = num // 4
        return num == 1


num = 16
s = Solution()
print(s.isPowerOfFour(num))
