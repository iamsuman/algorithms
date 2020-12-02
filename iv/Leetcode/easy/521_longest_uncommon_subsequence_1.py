class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            return max(len(a), len(b))


a = "aba"; b = "cdc"
# a = "aaa"; b = "aaa"
s = Solution()
print(s.findLUSlength(a,b))
