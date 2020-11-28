class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            sign = "-"
            num = abs(num)
        else:
            sign = ""

        res = ""
        while num > 0:
            res = str(num % 7) + res
            num = num // 7

        return sign + res


num = 100
# num = -7
num = 0
num = 7
s = Solution()
print(s.convertToBase7(num))





