class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        popen = 0
        res = ""
        for i in range(len(s)):
            if popen == 0:
                if s[i] == "(":
                    popen += 1
                else:
                    res += s[i]
            else:
                if s[i] == "(":
                    popen += 1
                    res += s[i]
                else:
                    if popen != 1:
                        res += s[i]
                    popen -= 1
        return res


s = "(()())(())"
s = "(()())(())(()(()))"
s = "()()"
s = ""
sol = Solution()
print(sol.removeOuterParentheses(s))




