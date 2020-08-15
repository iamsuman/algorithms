"""
Given 2 sorted arrays, find all the elements which occur in both the arrays.
"""


class Solution():
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        i = 0
        j = 0
        res = []
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                res.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
        return res


A = [1, 2, 3, 3, 4, 5, 6]
B = [3, 3, 5]
s = Solution()
print(s.intersect(A, B))
