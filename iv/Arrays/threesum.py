class Mysum():
    def threesum(self, A):
        n = len(A)
        result = []
        for i in range(n):
            j = i + 1
            while j < n - 1:
                k = j + 1
                while k < n:
                    if A[i] + A[j] + A[k] == 0:
                        B = sorted([A[i], A[j], A[k]])
                        if not B in result:
                            result.append(B)
                    k = k + 1
                j = j + 1
        return sorted(result)

    def threesum1(self, A):
        ret = []
        A.sort()
        for i in range(len(A)):
            if A[i] > 0:
                break
            if A[i] != A[i - 1]:
                self.twosum(A, i, ret)
        return ret

    def twosum(self, A, i, ret):
        low, hi = i + 1, len(A) - 1
        while low < hi:
            mysum = A[i] + A[low] + A[hi]
            if mysum < 0:
                low = low + 1
            elif mysum > 0:
                hi = hi - 1
            else:
                ret.append([A[i], A[low], A[hi]])
                low = low + 1
                hi  = hi - 1






A = [-1, 0, 1, 2, -1, -4]
a = Mysum()
# print(a.threesum(A))
print(a.threesum1(A))





