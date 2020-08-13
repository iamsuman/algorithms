"""
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
"""


class Solution():
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        # two cases
        # (A[i] + i) - (A[j] + j)
        # (A[i] - i) - (A[j] - j)

        m = 2 ** 32 - 1
        max1 = -1 * m
        min1 = m
        max2 = -1 * m
        min2 = m

        for i in range(len(A)):
            a = A[i] + i
            b = A[i] - i
            if a > max1:
                max1 = a
            if a < min1:
                min1 = a

            if b > max2:
                max2 = b
            if b < min2:
                min2 = b
        #     print(max1, min1, max2, min2)
        # print(max1, min1, max2, min2)

        return max(max1 - min1, max2 - min2)

    def slow_maxArr(self, A):
        # bruteforce
        maxsum = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                mysum = self.fsum(A, i, j)
                if mysum > maxsum:
                    maxsum = mysum
        return maxsum

    def fsum(self, A: list, i, j):
        return abs(A[i] - A[j]) + abs(i - j)


s = Solution()
A = [1, 3, -1]
A = [-98, -5, 37, -97, 38, 22, 70, 42, 61, 84]
print(s.maxArr(A))
print(s.slow_maxArr(A))
