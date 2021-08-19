class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            val = columnNumber % 26
            if val == 0:
                val += 26
                columnNumber = columnNumber // 26 - 1
            else:
                columnNumber = columnNumber // 26
            res = chr(val + 64) + res
        return res


columnNumber = 1
columnNumber = 52
# columnNumber = 28
columnNumber = 2147483647
# columnNumber = 701
# columnNumber = 286
s = Solution()
print(s.convertToTitle(columnNumber))
