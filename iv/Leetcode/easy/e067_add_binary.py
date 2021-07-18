class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)-1
        n = len(b)-1
        carry = 0
        res = ""
        while m >= 0 and n >= 0:
            summ = int(a[m]) + int(b[n]) + carry
            if summ == 0:
                res = "0" + res
                carry = 0
            elif summ == 1:
                res = "1" + res
                carry = 0
            elif summ == 2:
                res = "0" + res
                carry = 1
            else:
                res = "1" + res
                carry = 1
            m -= 1
            n -= 1

        while m >= 0:
            summ = int(a[m]) + carry
            if summ == 0:
                res = "0" + res
                carry = 0
            elif summ == 1:
                res = "1" + res
                carry = 0
            elif summ == 2:
                res = "0" + res
                carry = 1
            else:
                res = "1" + res
                carry = 1
            m -= 1

        while n >= 0:
            summ = int(b[n]) + carry
            if summ == 0:
                res = "0" + res
                carry = 0
            elif summ == 1:
                res = "1" + res
                carry = 0
            elif summ == 2:
                res = "0" + res
                carry = 1
            else:
                res = "1" + res
                carry = 1
            n -= 1

        if carry == 1:
            res = "1" + res
        return res


a = "11"; b = "1"
a = "1010"; b = "1011"
s = Solution()
print(s.addBinary(a, b))

