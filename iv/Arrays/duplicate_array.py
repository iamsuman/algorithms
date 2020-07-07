class Duplicate():
    def duplicate_array(self, A):
        # A = [1, 2, 3, 3, 4, 4, 5]
        n = len(A)
        start = 0
        end = 0
        while start < n - 2:
            if A[start] < A[start + 1]:
                start = start + 1
                continue
            else:
                for end in range(start + 1, n):
                    if A[start] >= A[end]:
                        continue
                    else:
                        A[start + 1] = A[end]
                        break
            start = start + 1
        return A

