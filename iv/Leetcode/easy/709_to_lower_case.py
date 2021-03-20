class Solution:
    def toLowerCase(self, str: str) -> str:
        res = []
        for i in range(len(str)):
            if 65 <= ord(str[i]) <= 92:
                res.append(chr(ord(str[i]) + 32))
            else:
                res.append(str[i])
        return "".join(res)

    def toLowerCase2(self, str: str) -> str:
        s = "".join([chr(i) for i in range(65, 91)])
        t = "".join([chr(i) for i in range(97,123)])
        res = []
        for i in range(len(str)):
            # ind = s.index(str[i])
            if str[i] in s:
                ind = s.index(str[i])
                res.append(t[ind])
            else:
                res.append(str[i])
        return "".join(res)



str = "Hello"
str = "here"
# str = "i797"
str = ""
s = Solution()
print(s.toLowerCase(str))
print(s.toLowerCase2(str))
