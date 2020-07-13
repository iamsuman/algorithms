class Combo():
    def combine(self,n, k):
        A = list(range(1,n + 1))
        res = self.comb(A, k)
        return res

    def comb(self, A, n):
        if n == 0:
            return [[]]
        l = []
        for i in range(0, len(A)):
            m = A[i]
            remLst = A[i + 1:]
            for p in self.comb(remLst, n - 1):
                l.append([m] + p)
        return l


def combinations(n, list, combos=[]):
    # initialize combos during the first pass through
    if combos is None:
        combos = []

    if len(list) == n:
        # when list has been dwindeled down to size n
        # check to see if the combo has already been found
        # if not, add it to our list
        if combos.count(list) == 0:
            combos.append(list)
            combos.sort()
        return combos
    else:
        # for each item in our list, make a recursive
        # call to find all possible combos of it and
        # the remaining items
        for i in range(len(list)):
            refined_list = list[:i] + list[i+1:]
            combos = combinations(n, refined_list, combos)
        return combos





a = Combo()
A = 4
B = 2

# print(a.combine(A,B))
print(a.comb([1,2,3,4], 2))
print(a.comb([1,2,3,4,5], 2))



