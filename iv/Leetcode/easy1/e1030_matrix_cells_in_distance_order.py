from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        mat = []
        for i in range(rows):
            mat.append([0] * cols)
        # print(mat)
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = [i, j]
        # print(mat)
        res_array = []
        for i in range(rows):
            for j in range(cols):
                dist = abs(mat[i][j][0] - rCenter) + abs(mat[i][j][1] - cCenter)
                res_array.append([dist, mat[i][j]])
        res_array.sort(key=lambda x: x[1])
        res = []
        for arr in res_array:
            res.append(arr[1])
        return res


rows = 1; cols = 2; rCenter = 0; cCenter = 0
rows = 2; cols = 2; rCenter = 0; cCenter = 1
s = Solution()
print(s.allCellsDistOrder(rows, cols, rCenter, cCenter))
