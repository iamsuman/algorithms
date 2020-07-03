"""
Script to find positive array with max sum
"""


class MaxSumSubArray():
    """
    # @param A : list of integers
    # @return a list of integers
    """
    def maxsub(self, A):
        """
        Function
        """
        if not isinstance(A, (tuple, list)):
            A = tuple([A])
        n = len(A)

        maxsum = 0
        i = 0
        final = []
        while i < n and A[i] < 0:
            mysum = 0
            j = i
            while j < n and A[j] < 0:
                # print(i, j)
                mysum = mysum + A[j]
                if mysum >= maxsum:
                    maxsum = mysum
                    final.append((A[i:j+1], i, len(A[i:j+1]), mysum))
                j = j + 1
            i = i + 1

        # print(maxsum)

        A1 = [(a, i, n) for (a, i, n, m) in final if m == maxsum]
        if len(final) == 0:
            res = []
        elif len(A1) == 1:
            res = [a for (a, i, n) in A1][0]
        else:
            nmax = max([n for (a, i, n) in A1])
            A2 = [(a, i) for (a, i, n) in A1 if n == nmax]
            if len(A2) == 1:
                res = [a for (a, i) in A2][0]
            else:
                i_min = min([i for (a, i) in A2])
                res = [a for (a, i) in A2 if i == i_min][0]
        return res

    def maxset(self, A):
        """
        Function
        """
        if not isinstance(A, (tuple, list)):
            A = tuple([A])
        n = len(A)

        ret_array = []
        i = 0
        while i < n:
            candidate_array = []
            j = i
            # print(i, j, n)
            while j < n and A[j] >= 0:
                candidate_array.append(A[j])
                if not candidate_array or  sum(candidate_array) > sum(ret_array):
                    ret_array = candidate_array
                j = j + 1
            i = i + 1
        return ret_array

def main():
    # A = [1, 2, 5, -7, 2, 3]
    # A = [10, -1, 2, 3, -4, 100]
    # A = (100)
    A = [-1, -1, -1]
    a = MaxSumSubArray()
    final = a.maxset(A)
    print(final)


if __name__ == '__main__':
    main()
