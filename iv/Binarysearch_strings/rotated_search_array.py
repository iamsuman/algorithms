class Rotated_Search():
    def search(self, A, B):
        n = len(A)
        pivot = self.find_pivot(A, 0, n - 1)
        # A = [4, 5, 6, 7, 0, 1, 2, 3]
        # B = 4
        # print(pivot)

        if pivot == -1:
            return self.binary_search(A, 0, n - 1, B)

        if A[pivot] == B:
            return pivot
        if B < A[0]:
            return self.binary_search(A, pivot + 1, n - 1, B)
        else:
            return self.binary_search(A, 0, pivot - 1, B)

    def find_pivot(self, A, low, hi):
        if low > hi:
            return -1
        if low == hi:
            return low

        mid = int((low + hi) / 2)

        if mid < hi and A[mid] > A[mid + 1]:
            return mid
        if mid > low and A[mid] < A[mid - 1]:
            return (mid - 1)
        if A[low] >= A[mid]:
            return self.find_pivot(A, low, mid - 1)
        else:
            return self.find_pivot(A, mid + 1, hi)

    def binary_search(self, A, low, hi, key):
        if hi < low:
            return -1
        mid = int((hi + low) / 2)

        if key == A[mid]:
            return mid
        if key > A[mid]:
            return self.binary_search(A, mid + 1, hi, key)
        else:
            return self.binary_search(A, low, mid - 1, key)


A = [4, 5, 6, 7, 0, 1, 2, 3]
A = [0,1,2,3,4,5,6,7]

B = 4

A = [ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ]
B = 202
a = Rotated_Search()
print(a.search(A, B))
