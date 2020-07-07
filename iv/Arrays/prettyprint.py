class Pretty():
    def prettyprint(self, n):
        s = 2 * n -1
        A = [[0] * s for _ in range(s)]

        start = 0
        end = 2 * n - 2
        k = n
        while k > 0:
            for i in range(start,end + 1):
                for j in range(start, end + 1):
                    if i == start or i == end or j == start or j == end:
                        A[i][j] = k
            k = k - 1
            start = start + 1
            end = end - 1
        return A

    def prettyPrint(self, n):
        # number of rows and columns to be printed
        s = 2 * n - 1

        # Upper Half
        for i in range(0, int(s / 2) + 1):
            m = n
            # Decreasing part
            for j in range(0, i):
                print(m, end=" ")
                m -= 1
            # Constant Part
            for k in range(0, s - 2 * i):
                print(n - i, end=" ")
                # Increasing part.
            m = n - i + 1
            for l in range(0, i):
                print(m, end=" ")
                m += 1
            print("")
            # Lower Half
        for i in range(int(s / 2), -1, -1):
            # Decreasing Part
            m = n
            for j in range(0, i):
                print(m, end=" ")
                m -= 1
            # Constant Part.
            for k in range(0, s - 2 * i):
                print(n - i, end=" ")
                # Decreasing Part
            m = n - i + 1
            for l in range(0, i):
                print(m, end=" ")
                m += 1

            print("")

    def myprint(self, A):
        for i in range(len(A)):
            for j in range(len(A)):
                print(A[i][j], end=" ")
            print("")





a = Pretty()
# A = a.prettyPrint(3)
A = a.prettyprint(3)

a.myprint(A)
