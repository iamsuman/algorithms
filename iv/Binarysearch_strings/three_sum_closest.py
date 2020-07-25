class Solution():
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        closest = 2 ** 64 - 1
        res = 0
        for i in range(len(A)):
            remA = A[:i] + A[i+1:]
            closest_sum = self.twosum(remA, A[i], B)
            if abs(closest_sum - B) < closest:
                closest = abs(closest_sum - B)
                res = closest_sum
        return res

    def twosum(self, A, i, B):
        start = 0
        end = len(A) - 1
        closest = 2 ** 64 - 1
        res = 0
        while start < end:
            mysum = i + A[start] + A[end]
            if abs(mysum - B) < closest:
                closest = abs(mysum - B)
                res = mysum
            if mysum < B:
                start = start + 1
            if mysum > B:
                end = end - 1
            if closest == 0:
                return mysum
        return res

s = Solution()
A = [-1, 2, 1, -4]
B = 1

# A = [ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ]
# B = -1

# A = [ 2147483647, -2147483648, -2147483648, 0, 1 ]
# B = 0

A = [ -10, -10, -10 ]
B = -5

print(s.threeSumClosest(A,B))

