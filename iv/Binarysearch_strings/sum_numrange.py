class Numrange_sum():
    """
    Given an array of non negative integers A, and a range (B, C),
find the number of continuous subsequences in the array which have sum S in the range [B, C] or B <= S <= C
    """

    def numrange(self, A, B, C):
        sumrange = list(range(B, C + 1))
        start = 0
        n = len(A)
        ret = []

        while start < n - 1:
            mysum = A[start]
            if mysum > max(sumrange):
                start = start + 1
                continue
            end = start + 1
            while end < n:
                mysum = mysum + A[end]
                if mysum in sumrange:
                    ret.append(A[start:end + 1])
                    end = end + 1
                elif mysum > C:
                    break
                else:
                    end = end + 1
            start = start + 1
        print(ret)
        # print(sumrange)
        return len(ret)

    def numrange2(self, A, B, C):
        sumrange = list(range(B, C + 1))
        start = 0
        n = len(A)
        ret = []

        while start < n:
            mysum = 0
            end = start
            while end < n:
                mysum = mysum + A[end]
                if mysum in sumrange:
                    ret.append(A[start:end + 1])
                    end = end + 1
                elif mysum > C:
                    # start = start + 1
                    break
                else:
                    end = end + 1
            start = start + 1
        # print(ret)
        # print(sumrange)
        return len(ret)


# A = [10, 5, 1, 0, 2]
# B, C = 6, 8

# A = [10, 5, 1, 0, 2]
# B, C = 15, 20

# A = [1, 4, 6]
# B = 3
# C = 8

A = [ 76, 22, 81, 77, 95, 23, 27, 35, 24, 38, 15, 90, 19, 46, 53, 6, 77, 96, 100, 85, 43, 16, 73, 18, 7, 66 ]
B = 98
C = 290

a = Numrange_sum()
print(a.numrange2(A, B, C))
