class Solution:
    def findCenter(self, edges: list) -> int:
        res = []
        i, j = edges[0]
        if i in edges[1]:
            return i
        else:
            return j
        # for x, y in edges[1:]:
        #     if i == x or i == y:
        #         res.append(i)
        #     else:
        #         if i in res:
        #             res.pop(i)
        #     if j == x or j == y:
        #         res.append(j)
        #     else:
        #         if j in res:
        #             res.pop(j)
        #
        # x = list(set(res))
        # return x[0]


edges = [[1,2],[2,3],[4,2]]
# edges = [[1,2],[5,1],[1,3],[1,4]]
s = Solution()
print(s.findCenter(edges))
