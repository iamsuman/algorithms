"""
Given an array and a value, remove all the instances of that value in the array.
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.
"""
class Solution():
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        j = 0
        for i in range(len(A)):
            if A[i] != B:
                A[j] = A[i]
                j += 1
        return j

    def removeElement2(self, A, B):
        # TODO
        # Time complexity

        start = 0
        res = 0

        while start < len(A):
            if A[start] != B:
                start = start + 1
                continue
            else:
                end = start + 1
                found = False
                while end < len(A):
                    if A[end] != B:
                        A[start], A[end] = A[end], A[start]
                        found = True
                        break
                    end = end + 1
                if not found:
                    break
            start = start + 1
        # print(A)
        return start



    def removeElement3(self, A, B):
        # Order is mot matched
        start = 0
        end = len(A) - 1
        while start < end:
            if A[end] == B:
                end = end - 1
                continue
            if A[start] == B:
                A[start], A[end] = A[end], A[start]
            start = start + 1
        return start

A = [4, 1, 1, 2, 1, 3]
B = 1

# A = [ 1, 3, 3, 2, 1 ]
# B = 0
#
A = [ 2, 0, 1, 2, 0, 3, 2, 2, 2, 1, 0, 0, 0, 1, 0, 0, 2, 2, 2, 3, 2, 3, 1, 2, 1, 2, 2, 3, 2, 3, 0, 3, 0, 2, 1, 2, 0, 0, 3, 2, 3, 0, 3, 0, 2, 3, 2, 2, 3, 1, 3, 3, 0, 3, 3, 0, 3, 3, 2, 0, 0, 0, 0, 1, 3, 0, 3, 1, 3, 1, 0, 2, 3, 3, 3, 2, 3, 3, 2, 2, 3, 3, 3, 1, 3, 2, 1, 0, 0, 0, 1, 0, 3, 2, 1, 0, 2, 3, 0, 2, 1, 1, 3, 2, 0, 1, 1, 3, 3, 0, 1, 2, 1, 2, 2, 3, 1, 1, 3, 0, 2, 2, 2, 2, 1, 0, 2, 2, 2, 1, 3, 1, 3, 1, 1, 0, 2, 2, 0, 2, 3, 0, 1, 2, 1, 1, 3, 0, 2, 3, 2, 3, 2, 0, 2, 2, 3, 2, 2, 0, 2, 1, 3, 0, 2, 0, 2, 1, 3, 1, 1, 0, 0, 3, 0, 1, 2, 2, 1, 2, 0, 1, 0, 0, 0, 1, 1, 0, 3, 2, 3, 0, 1, 3, 0, 0, 1, 0, 1, 0, 0, 0, 0, 3, 2, 2, 0, 0, 1, 2, 0, 3, 0, 3, 3, 3, 0, 3, 3, 1, 0, 1, 2, 1, 0, 0, 2, 3, 1, 1, 3, 2 ]
B = 2


# [4, 1, 1, 2, 1, 3]
# 0/5 4 1 1 2 1 3
# 1/5 4 3 1 2 1 1
# 2/5
# 2/4
# 3/4 4 3 2 1 1 1
# 4 4

s = Solution()
print(s.removeElement(A, B))



