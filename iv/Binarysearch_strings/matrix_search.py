"""
Given a matrix of integers A of size N x M and an integer B.

Write an efficient algorithm that searches for integar B in matrix A.

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
"""
class Solution():
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        n = len(A)
        found = False
        rowmin, rowmax = 0, n - 1
        while rowmin <= rowmax:
            mid = int(rowmin + (rowmax - rowmin)/2)
            # print(A[mid][0])
            if A[mid][0] == B:
                return 1
            elif A[mid][0] > B:
                rowmax = mid - 1
            else:
                if A[mid][-1] < B:
                    rowmin = mid + 1
                else:
                    break
        row = mid
        # print(row)

        m = len(A[mid])
        colmin, colmax = 0, m - 1
        while colmin <= colmax:
            mid = int((colmin + colmax)/2)
            if A[row][mid] == B:
                # print(row,mid)
                return 1
            elif A[row][mid] > B:
                colmax = mid -1
            else:
                colmin = mid + 1

        return 0

A =[ [2, 3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]]
B = 50

# A = [
#   [3],
#   [29],
#   [36],
#   [63],
#   [67],
#   [72],
#   [74],
#   [78],
#   [85]
# ]
# B = 41
s = Solution()
print(s.searchMatrix(A, B))









