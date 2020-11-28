"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
"""
class Solution():
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        count = [0 for i in range(27)]
        for i in tiles:
            count[ord(i) - ord('A') + 1] += 1
        # print(count)
        res = []

        # TODO create string for results
        val = self.dfs(count, res)
        # print(res)
        return val

    def dfs(self, count, res):
        # TODO

        res = []
        summ = 0
        for i in range(1, 27):
            if count[i] == 0:
                continue
            count[i] -= 1
            res.append(count[i])
            summ += 1
            summ += self.dfs(count, res)
            count[i] += 1
        return summ



A = "AAB"
s = Solution()
print(s.numTilePossibilities(A))
