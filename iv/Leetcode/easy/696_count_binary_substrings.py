class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        grp = []
        count = 0
        for i in range(len(s)):
            if count == 0:
                count += 1
                continue
            if s[i] == s[i-1]:
                count += 1
            else:
                grp.append(count)
                count = 1
        grp.append(count)
        # print(grp)

        res = 0
        for i in range(len(grp)-1):
            res += min(grp[i], grp[i+1])
        return res



s = "00110011"
s = "10101"
sol = Solution()
print(sol.countBinarySubstrings(s))
