import time
class Solution:
    def isToeplitzMatrix(self, matrix: list) -> bool:
        row = len(matrix)
        if row > 0:
            col = len(matrix[0])
        else:
            return False

        for j in range(col):
            ii = 0
            c = matrix[ii][j]
            jj = 0
            while j + jj < col and ii < row:
                if matrix[ii][j+jj] != c:
                    return False
                jj += 1
                ii += 1
        for i in range(row):
            jj = 0
            c = matrix[i][jj]
            ii = 0
            while i + ii < row and jj < col:
                if matrix[i+ii][jj] != c:
                    return False
                ii += 1
                jj += 1
        return True

    def isToeplitzMatrix2(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r - c not in groups:
                    groups[r - c] = val
                elif groups[r - c] != val:
                    return False
        return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
matrix = [[1,2],[2,2]]
s = Solution()
s1 = time.time()
print(s.isToeplitzMatrix(matrix))
s2 = time.time()
print(s.isToeplitzMatrix2(matrix))
s3 = time.time()
print(s2 -s1, s3 - s2)

