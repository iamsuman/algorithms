class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for ss in stones:
            if ss in jewels:
                count += 1
        return count


jewels = "aA"; stones = "aAAbbbb"
jewels = "z"; stones = "ZZ"
s = Solution()
print(s.numJewelsInStones(jewels, stones))
