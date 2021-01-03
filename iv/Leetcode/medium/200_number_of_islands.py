class Solution:
    def numIslands(self, grid: list) -> int:
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        # print(m, n)
        islands = 0
        res = []
        for i in range(m):
            res.append([0] * n)

        def island_extend(ii, jj):
            grid[ii][jj] = "0"
            # print(grid)
            if ii - 1 >= 0 and grid[ii - 1][jj] == "1":
                points.append([ii - 1, jj])
                grid[ii - 1][jj] = "0"
            # top
            if jj - 1 >= 0 and grid[ii][jj - 1] == "1":
                points.append([ii, jj - 1])
                grid[ii][jj - 1] = "0"
            # bottom
            if ii + 1 < m and grid[ii + 1][jj] == "1":
                points.append([ii + 1, jj])
                grid[ii + 1][jj] = "0"
            # right
            if jj + 1 < n and grid[ii][jj + 1] == "1":
                points.append([ii, jj + 1])
                grid[ii][jj + 1] = "0"

        for i in range(m):
            for j in range(n):
                # print(grid)
                if grid[i][j] == "0":
                    continue

                islands += 1
                grid[i][j] = "0"
                # print(i,j)
                points = [[i,j]]
                for [x, y] in points:
                    # print(points)
                    # print(x,y)
                    island_extend(x, y)
        return islands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
grid = []
grid = [["1", "1", "1"]]
grid = [["1","1"]]
grid = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
s = Solution()
print(s.numIslands(grid))

