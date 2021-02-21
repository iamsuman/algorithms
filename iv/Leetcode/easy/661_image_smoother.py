class Solution:
    def imageSmoother(self, M: list) -> list:
        l = len(M)
        if l == 0:
            return M
        m = len(M[0])
        res = []
        for i in range(l):
            res.append([0] * m)
        # print(res)
        for x in range(l):
            for y in range(m):
                summ = 0
                count = 0
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        if 0 <= i < l and 0 <= j < m:
                            summ += M[i][j]
                            count += 1
                res[x][y] = int(summ / count)
        return res


M = [[1,1,1],
     [1,0,1],
     [1,1,1]]
s = Solution()
print(s.imageSmoother(M))
