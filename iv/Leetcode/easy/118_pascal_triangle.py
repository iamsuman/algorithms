from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                d = [1]
                for j in range(len(res[i - 1]) -1):
                    d.append(res[i - 1][j] + res[i - 1][j + 1])
                d.append(1)
                res.append(d)
        return res


numRows = 5
s = Solution()
print(s.generate(numRows))
