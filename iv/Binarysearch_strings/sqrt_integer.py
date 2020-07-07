class Mysqrt():
    def sqrt_integer(self, A):
        if A == 0:
            return 0
        if A == 1:
            return 1
        i = int(A/2)
        while i * i > A:
            i = i - 1
        return i

    def sqrt_integer2(self, A):
        if A == 0:
            return 0
        if A == 1:
            return 1
        mymax = A
        mymin = 1
        i = int(A/2)
        while mymax - mymin > 1:
            if i * i > A:
                mymax = i
            else:
                mymin = i
            i = int((mymax + mymin) / 2)
        return mymin


a = Mysqrt()
# print(a.sqrt_integer2(4))
print(a.sqrt_integer2(30506))




