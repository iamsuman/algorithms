class Next():
    def nextPermutation(self, A):
        # A = [ 1, 2, 7, 5, 6, 1]
        n = len(A)
        # find the Index

        myindex = -1
        i = n - 2
        while i >= 0:
            if A[i] < A[i + 1]:
                myindex = i
                break
            i = i - 1

        print(myindex)
        if myindex == -1:
            return sorted(A)
        else:
            B = A[myindex + 1:]
            m = self.find_next_max_index(A[myindex], B)
            A[myindex], A[myindex + 1 + m] = A[myindex + 1 + m], A[myindex]
            A1 = A[:myindex + 1]
            A2 = A[myindex + 1:]
            A2.sort()
            A = A[:myindex + 1] + A2
        return A

    def find_next_max_index(self, p, B):
        greater = False
        next_max = -1
        for i in range(len(B)):
            if B[i] > p:
                if greater:
                    next_max = min([next_max, B[i]])
                else:
                    next_max = B[i]
                    greater = True
        return B.index(next_max)


# A = [6, 2, 1, 5, 4, 3, 0]
# A = [1,2,1]
A = [3,2,1]
a = Next()
print(a.nextPermutation(A))
