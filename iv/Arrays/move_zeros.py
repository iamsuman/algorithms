class Move():
    def move_zeros(self, A):
        # A = [0,1,0,3,12]
        n = len(A)
        i = 0
        zeros = True
        while i < n - 1:
            if A[i] == 0:
                if A[i + 1] != 0:
                    A[i], A[i+1] = A[i+1], A[i]
                else:
                    start = i + 2
                    end = n

                    while start < end:
                        if A[start] != 0:
                            print(start, i)
                            A[i], A[start] = A[start], A[i]
                            zeros = False
                            break
                        start = start + 1
                    if zeros:
                        break

            i = i + 1
        return A



A = [0,1,0,3, 0,12]
# A = [0,1]
a = Move()
print(a.move_zeros(A))
