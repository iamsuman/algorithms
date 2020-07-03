class Duplicate():
    def repeatedNumber(self, A):
        # A = [3 4 1 4 1]
        B = []
        for i in A:
            if i in B:
                return i
            else:
                B.append(i)
        if len(B) == 0:
            return -1

    def repeatedNumber2(self, A):
        B = list(A)
        B.sort()
        repeat = False
        for i in range(len(B)):
            if B[i] == B[i + 1]:
                return B[i]
        if not repeat:
            return -1






