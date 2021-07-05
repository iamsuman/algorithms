from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo, hi = 0, len(s)
        ans = [0] * (hi+1)
        for i in range(len(s)):
            if s[i] == "I":
                ans[i] = lo
                lo += 1
            else:
                ans[i] = hi
                hi -= 1

        ans[len(s)] = lo
        return ans


s = "IDID"
s = "III"
sol = Solution()
print(sol.diStringMatch(s))

