class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            res = res * 26 + ord(columnTitle[i]) - 64
        return res


columnTitle = "A"
columnTitle = "AB"
columnTitle = "ZY"
columnTitle = "FXSHRXW"
s = Solution()
print(s.titleToNumber(columnTitle))

