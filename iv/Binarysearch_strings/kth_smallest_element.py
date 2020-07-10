class Kmin():
    def kthBiggest(self, A, B):
        myheap = []
        while len(myheap) < B:
            i = 0
            mymax = -1

            for j in range(len(A)):
                if A[j] > mymax and A[j] not in myheap:
                    mymax = A[j]
            temp_array = []
            for j in range(len(A)):
                if A[j] == mymax:
                    temp_array.append(A[j])
                if len(temp_array) + len(myheap) > B:
                    break
            myheap = myheap + temp_array

        return myheap[B - 1]

    def kthsmallest(self, A, B):
        myheap = []
        while len(myheap) < B:
            i = 0
            mymin = max(A) * 10

            for j in range(len(A)):
                if A[j] < mymin and A[j] not in myheap:
                    mymin = A[j]
            temp_array = []
            for j in range(len(A)):
                if A[j] == mymin:
                    temp_array.append(A[j])
                if len(temp_array) + len(myheap) > B:
                    break
            myheap = myheap + temp_array

        return myheap[B - 1]

    def kthsmallest3(self, A, B):
        myheap = []
        while len(myheap) < B:
            i = 0
            mymin = max(A) + 1

            for j in range(len(A)):
                if A[j] < mymin and A[j] not in myheap:
                    mymin = A[j]
                    i = 1
                elif A[j] == mymin and A[j] not in myheap:
                    i = i + 1
            # print(mymin, i)
            temp_array = [mymin] * i
            # temp_array = []
            # for j in range(len(A)):
            #     if A[j] == mymin:
            #         temp_array.append(A[j])
            #     if len(temp_array) + len(myheap) > B:
            #         break
            myheap = myheap + temp_array

        return myheap[B - 1]


# A = [2, 1, 4, 3, 2]
# B = 3

A = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
B = 9

# A = [ 47, 7 ]
# B = 2

a = Kmin()
print(a.kthsmallest3(A, B))






