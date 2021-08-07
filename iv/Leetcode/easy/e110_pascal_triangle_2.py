from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1], [1,1]]
        for i in range(2, rowIndex + 1):
            d = [1]
            for j in range(1, i):
                d.append(res[i-1][j-1] + res[i-1][j])
            d.append(1)
            res.append(d)
        return res[rowIndex]


rowIndex = 3
rowIndex = 0
rowIndex = 1
rowIndex = 33
s = Solution()
print(s.getRow(rowIndex))
