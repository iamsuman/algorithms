from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        for i in range(n):
            res.append([0] * m)
        # print(res)
        for i in range(n):
            for j in range(m):
                res[i][j] = matrix[j][i]

        return res


matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3],[4,5,6]]
# matrix = [1,2,3]
s = Solution()
print(s.transpose(matrix))



