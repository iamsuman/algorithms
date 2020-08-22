"""
Max Unsorted array which if sorted, entire array will become sorted

"""
class Solution():
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        b = sorted(A)  # sorted form of A is B
        if (A == b):
            return [-1]
        else:
            # LIST OF ALL POINTS WHICH ARE NOT IN CORRECT PLACE
            L = [i for i in range(len(A)) if A[i] != b[i]]
            # print(L)
            return [min(L), max(L)]

    def sunUnsort2(self, A):
        start = -1
        end = -1
        for i in range(len(A)):
            if start == -1:
                if i != len(A) - 1 and A[i] > min(A[i + 1:]):
                    start = i
            if start != -1 and i != len(A) - 1:
                a = max(A[start:i + 1])
                b = min(A[i + 1:])
                if max(A[start:i + 1]) > min(A[i + 1:]):
                    end = i + 1
        if start == -1:
            return [-1]
        else:
            if end == -1:
                end = i
            return [start, end]


A = [1, 3, 2, 4, 5]
A = [1, 2, 3, 4, 5]
A = [1, 4, 2, 3, 5]
A = [ 1, 2, 5, 4, 6, 3]
A = [ 1, 1, 10, 10, 15, 10, 15, 10, 10, 15, 10, 15 ]
A = [ 3, 3, 4, 5, 5, 9, 11, 13, 14, 15, 15, 16, 15, 20, 16 ]
s = Solution()
print(s.subUnsort(A))



