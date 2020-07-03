class Maxsum():
    def sumsubarray(self, A, B):
        n = len(A)
        maxsum = -100 * n - 1
        i = 0
        j = 0
        while i < n - B + 1:
            j = 0
            while j < n - B + 1:
                # print(i,j)
                mysum = 0
                for ii in range(B):
                    for jj in range(B):
                        # print(i + ii, j + jj)
                        mysum = mysum + A[i + ii][j + jj]
                # print(mysum)
                if mysum > maxsum:
                    maxsum = mysum
                j = j + 1
            i = i + 1
        return maxsum

    def sumsubarray2(self, A, B):
        n = len(A)

        stripsum = [[False] * (n)] * (n-B+1)
        print(stripsum)

        for i in range(n - B + 1):
            for j in range(n):

                mysum = 0
                for k in range(B):
                    mysum = mysum + A[i + k][j]

                print(i,j)
                print(mysum)
                stripsum[i][j] = mysum
                print(stripsum)
        print(stripsum)
        print("\n\n\n")

        maxsum = -100 * n - 1
        for i in range(n - B + 1):
            for j in range(n - B + 1):
                mysum = 0
                for k in range(B):
                    mysum = mysum + stripsum[i][j + k]
                if mysum > maxsum:
                    maxsum = mysum
        return maxsum


A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
A = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 8, 6, 7, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5]
     ]
a = Maxsum()
# print(a.sumsubarray(A, 2))
print(a.sumsubarray2(A, 3))
