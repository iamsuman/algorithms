class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = self.absstr(s)
        t1 = self.absstr(t)
        # print(s1)
        if s1 == t1:
            return True
        else:
            return False

    def absstr(self, s: str):
        res = []
        for i in range(len(s)):
            if s[i] == "#":
                if len(res) != 0:
                    res.pop()
            else:
                res.append(s[i])
        return "".join(res)


s = "ab#c"; t = "ad#c"
s = "ab##"; t = "c#d#"
# s = "a##c"; t = "#a#c"
sol = Solution()
print(sol.backspaceCompare(s, t))


