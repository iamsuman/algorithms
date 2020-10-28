"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m = len(num1) - 1
        n = len(num2) - 1
        carry = 0
        res = []
        while m >= 0 or n >= 0:
            x1 = int(num1[m]) if m >= 0 else 0
            x2 = int(num2[n]) if n >= 0 else 0
            summ = x1 + x2 + carry
            if summ > 9:
                carry = 1
                summ = summ - 10
            else:
                carry = 0
            res.append(str(summ))
            m -= 1
            n -= 1
        if carry == 1:
            res.append("1")
        res.reverse()
        return "".join(res)

num1 = "999"; num2 = "1"
# num1 = "24"; num2 = "85"
s = Solution()
print(s.addStrings(num1, num2))




