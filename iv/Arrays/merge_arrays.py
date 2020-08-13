"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.
"""


class MergeArrays():
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A: list, B):
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] >= B[j]:
                A.insert(i, B[j])
                j = j + 1
                i = i + 1
            else:
                i = i + 1
        if j < len(B):
            A.extend(B[j:])
        return A


A = [1, 5, 8]
B = [6, 9]

A = [ 1, 2 ]
B = [ -1, 2 ]

A = [ -4, -3, 0 ]
B = [ 2 ]

s = MergeArrays()
print(s.merge(A,B))

