"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
"""


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # TODO Verify why input 5,7 is not matching with output 4
        bin_m = self.number_to_binary(m)
        bin_n = self.number_to_binary(n)
        print(bin_m, bin_n)

        min_len = min(len(bin_m), len(bin_n))

        res = ""
        i = 0
        while i < min_len:
            ii = len(bin_m) - min_len
            jj = len(bin_n) - min_len
            if bin_m[i + ii] == '1' and bin_n[i + jj] == '1':
                res = res + "1"
            else:
                res = res + "0"
            i += 1
        # print(self.number_to_binary(12))
        return int(res)

    def number_to_binary(self, a):
        if a == 0:
            return "0"
        res = ""
        while a > 0:
            res = str(a % 2) + res
            a = int(a / 2)
        return res

    def binary_to_num(self, a):
        if "a" == '0':
            return 0
        res = 0
        for i in range(len(a)):
            res = res * 2 + int(a[i])
        return res


A = 5
B = 7

A = 60            # 60 = 0011 1100
B = 13            # 13 = 0000 1101
ans = 12
s = Solution()
a = s.rangeBitwiseAnd(A, B)
print(a)
print(s.binary_to_num(str(a)))
