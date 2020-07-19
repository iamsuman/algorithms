class NumberArray:
    # @param A : list of integers
    # @return a list of integers
    # A = [1, 2, 3]
    def plusOne(self, A):
        n = len(A)
        i = n - 1
        carry = 0
        A[i] = A[i] + 1
        while i >= 0:
            A[i] = A[i] + carry
            if A[i] == 10:
                A[i] = 0
                carry = 1
            else:
                carry = 0
                break
            i = i - 1

        if i == -1 and carry == 1:
            A = [1] + A
        for i in range(len(A)):
            if A[i] == 0:
                continue
            else:
                break
        return A[i:]


A = [1, 2, 3]
A = [9, 9, 9]
A = [0, 0, 9, 9, 9]
a = NumberArray()
print(a.plusOne(A))
