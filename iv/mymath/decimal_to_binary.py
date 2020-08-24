"""
Given a number N >= 0, find its representation in binary.
"""
class Solution():
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        if A == 0:
            return 0
        res = ""
        while A > 0:
            res = str(A%2) + res
            A = int(A/2)

        return res

A = 125
A = 6
s = Solution()
print(s.findDigitsInBinary(A))

