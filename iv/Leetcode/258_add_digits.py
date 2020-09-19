"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
"""
class Solution():
    def addDigits(self, num: int):
        # Digitroot: https://en.wikipedia.org/wiki/Digital_root
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9
        
    def addDigits2(self, num: int) -> int:
        while num > 9:
            num = self.sum_digits(num)
        return num

    def sum_digits(self, num):
        summ = 0
        while num > 0:
            summ = summ + num % 10
            num = int(num / 10)
        return summ


num = 38
s = Solution()
print(s.addDigits(num))

