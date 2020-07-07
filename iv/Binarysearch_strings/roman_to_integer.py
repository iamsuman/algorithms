class Roman():
    def romanToInt(self, A):
        # myroman = [(I,1), (V, 5), (X, 10), (C, 100), (D, 500),(M, 1000)]
        myroman = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000}

        mylist = list(A)
        mylist_1 = list(map(lambda x: myroman[x], mylist))
        val = 0
        n = len(mylist)
        i = 0
        while i < n - 1:
            if mylist_1[i] >= mylist_1[i + 1]:
                val = val + mylist_1[i]
                i = i + 1
            else:
                val = val + mylist_1[i+1] - mylist_1[i]
                i = i + 2
        if i == n - 1:
            val = val + mylist_1[i]
        return val

A = "IV"
A = "XLVII"

a =  Roman()
print(a.romanToInt(A))

