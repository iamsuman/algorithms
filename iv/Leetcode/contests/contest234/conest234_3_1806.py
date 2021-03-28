class Solution:
    def evaluate(self, s: str, knowledge: list) -> str:
        d = {}
        for key, item in knowledge:
            d[key] = item
        res = ""
        start = 0
        end = -1
        for i in range(len(s)):
            if s[i] == "(":
                start = i
                res += s[end+1:i]
            elif s[i] == ")":
                end = i
                if d.get(s[start+1:end]):
                    res += d[s[start+1:end]]
                else:
                    res += "?"
        if end < len(s) - 1:
            res += s[end+1:]
        return res


s = "(name)is(age)yearsold"; knowledge = [["name","bob"],["age","two"]]
s = "hi(name)"; knowledge = [["a","b"]]
s = "(a)(a)(a)aaa"; knowledge = [["a","yes"]]
s = "(a)(b)"; knowledge = [["a","b"],["b","a"]]
s = "c"; knowledge = []
sol = Solution()
print(sol.evaluate(s, knowledge))




