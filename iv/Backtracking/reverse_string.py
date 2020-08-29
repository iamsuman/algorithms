class Solution():
    def reverseString(self, s: list):
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 0:
            return s
        else:
            return self.reverseString(s[1:]) + [s[0]]


A = ["h","e","l","l","o"]
s = Solution()
print(s.reverseString(A))
