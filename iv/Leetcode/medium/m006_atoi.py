class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        sign = 1
        found = 0
        if s == "":
            return 0
        for i in range(len(s)-1):
            if s[i] in "0123456789":
                found = 1
                res += s[i]
            elif s[i] in [" ","-","+"] and found == 1:
                found = 2
                break
            elif s[i] in ["-", "+"] and s[i + 1] not in "0123456789":
                found = 2
                break
            elif s[i] == "-" and s[i+1] in "0123456789":
                sign = -1
            elif s[i] == "+" and s[i+1] in "0123456789":
                sign = 1
            elif s[i] == " ":
                pass
            elif s[i] not in "0123456789-+":
                found = 2
                break
        if len(s) == 1:
            i = -1
        if s[i+1] in "0123456789" and found != 2:
            res += s[i+1]
        if res == "":
            return 0
        if len(res) >= len(str(2 ** 31)) and int(res) >= 2 ** 31:
            if sign == -1:
                res = -2 ** 31
            else:
                res = 2 ** 31 -1
        else:
            res = sign * int(res)
        return res


s = "   -42"
s = ""
s = "   "
s = "1"
s = "4193 with words"
s = "+-43"
s = "--42"
# s = "sss43-"
s = "00000-42a1234"
s = "2147483648"

sol = Solution()
print(sol.myAtoi(s))


