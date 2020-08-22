"""
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.
"""
class Solution():
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)
        n = len(A[0])

        row = set([])
        col = set([])
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    A[i][j] = 0
        return A


A = [   [1, 0, 1],
        [1, 1, 1],
        [1, 1, 1]   ]
s = Solution()
print(s.setZeroes(A))


