class Rotate():
    # @param A : list of list of integers
    # @return the same list modified
    def rotate_matrix(self, A):
        n = len(A)

        for i in range(n):
            for j in range(i, n):
                temp = A[i][j]
                A[i][j] = A[j][i]
                A[j][i] = temp

        for i in range(n):
            for j in range(int(n / 2)):
                temp = A[i][n - 1 - j]
                A[i][n - 1 - j] = A[i][j]
                A[i][j] = temp
        return A

    def rotate_matrix2(self, A):
        n = len(A)

        pass
        return A

    def print_matrix(self, A):
        n = len(A)
        for i in range(n):
            print("|", end=" ")
            for j in range(n):
                print(A[i][j], end=" ")
            print("|")

def main():
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    a = Rotate()
    B = a.rotate_matrix(A)

    a.print_matrix(B)




if __name__ == '__main__':
    main()
