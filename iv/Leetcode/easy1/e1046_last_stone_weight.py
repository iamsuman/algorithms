from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) > 1:
            stones.sort(reverse=True)
            # print(stones)
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            else:
                stones[1] = abs(stones[1] - stones[0])
                stones.pop(0)
            print(stones)
            if len(stones) > 1:
                self.lastStoneWeight(stones)
            # print(stones)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]


stones = [2, 7, 4, 1, 8, 1]
stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
stones = [1]
stones = [2,2]
s = Solution()
print(s.lastStoneWeight(stones))
