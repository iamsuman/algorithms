"""
Given a column title A as appears in an Excel sheet, return its corresponding column number.
Input: 28
Output: AB
"""


class Solution():
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):

        alphabets = [chr(i) for i in range(65, 91)]
        res = 0
        l = list(A)
        alpha = 1
        for i in l[::-1]:
            val = alphabets.index(i) + 1
            res = res + val * alpha
            alpha = alpha * 26
        return res

    def titleToNumber2(self, A):
        ans = 0
        for char in A:
            ans = ans * 26 + (ord(char) - ord('A') + 1)
        return ans

s = Solution()
print(s.titleToNumber("AB"))


