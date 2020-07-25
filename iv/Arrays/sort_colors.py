class Colors():
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        n = len(A)
        start = 0
        for col in [0,1,2]:
            while start < n -1:
                if A[start] <= col:
                    start = start + 1
                    continue
                end = start + 1
                while end < n:
                    if A[end] == col:
                        A[start], A[end] = A[end], A[start]
                        break
                    end = end + 1
                if end == n:
                    break
                start = start + 1
        return A


A = [0, 1, 2, 0, 1, 2]
A = [1,1,1,2,0,2]
# A = [0, 1, 2, 0, 1, 2, 1]
c = Colors()
print(c.sortColors(A))

