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
        s =
        while s == "Z"


str = "Hello"
str = "here"
str = "i797"
# str = ""
s = Solution()
print(s.toLowerCase(str))
