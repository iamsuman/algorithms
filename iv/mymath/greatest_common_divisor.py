"""
Given 2 non negative integers m and n, find gcd(m, n)
"""


class Solution():
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A > B:
            A, B = B, A
        while B != 0:
            temp = B
            B = B % A
            A = temp
        return A

    def gcd1(self, A, B):
        # Brute Force
        a_factor = self.factors(A)
        final = 1
        for i in a_factor:
            if B % i == 0:
                B = int(B / i)
                final = final * i
        return final

    def factors(self, A):
        res = []
        i = 2
        while A > 1:
            if A % i == 0:
                res.append(i)
                A = int(A / i)
            else:
                i += 1 if i % 2 == 0 else 2
        return res


m = 6
n = 9
s = Solution()
print(s.gcd(m,n))
