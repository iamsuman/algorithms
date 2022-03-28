from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1 = s[0]
        c2 = s[3]
        r1 = s[1]
        r2 = s[4]

        res = []
        for i in range(ord(c1), ord(c2)+1):
            for j in range(int(r1), int(r2)+1):
                res.append(chr(i) + str(j))
        return res


s = "K1:L2"
s = "A1:F1"
s = "A1:A8"
sol = Solution()
print(sol.cellsInRange(s))


