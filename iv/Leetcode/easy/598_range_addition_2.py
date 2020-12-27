class Solution:
    def maxCount(self, m: int, n: int, ops: list) -> int:
        arr = []
        for i in range(m):
            arr.append([0] * n)
        # print(arr)
        if len(ops) > 0:
            for [i, j] in ops:
                self.range_addition(arr, i, j)
                # print(arr)

        maxint = 0
        maxcount = 0
        for i in range(m):
            for j in range(n):
                if arr[i][j] == maxint:
                    maxcount += 1
                elif arr[i][j] > maxint:
                    maxint = arr[i][j]
                    maxcount = 1
        return maxcount

    def range_addition(self, arr, i, j):
        for ii in range(i):
            for jj in range(j):
                arr[ii][jj] += 1
        return arr

    def maxCount2(self, m: int, n: int, ops: list) -> int:
        if len(ops) == 0:
            return m * n
        M = sorted(ops, key=lambda x:x[0])[0][0]
        N = sorted(ops, key=lambda x: x[1])[0][1]
        return M * N


m = 3; n = 3; ops = [[2,2],[3,3]]
# m = 3; n = 3; ops = []
s = Solution()
print(s.maxCount(m,n,ops))
print(s.maxCount2(m,n,ops))


