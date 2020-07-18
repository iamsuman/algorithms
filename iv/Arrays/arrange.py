class Arrange():
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        n = len(A)
        for i in range(0, n):
            m = A[A[i]]
            A[i] += (m % n) * n

        # print(A)
        for i in range(0, n):
            A[i] = int(A[i] / n)

        return A


A = [3, 2, 0, 1]
a = Arrange()
print(a.arrange(A))
