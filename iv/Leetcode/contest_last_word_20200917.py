"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
"""
class Solution():
    def lengthOfLastWord(self, s: str) -> int:
        last_len = 0
        res = 0
        for i in range(len(s)):
            if s[i] == " ":
                res = 0
            else:
                res = res + 1
                last_len = res
        return last_len


s = "Hello World"
sol = Solution()
print(sol.lengthOfLastWord(s))

