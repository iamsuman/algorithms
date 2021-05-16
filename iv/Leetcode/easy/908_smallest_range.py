from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxm = max(nums)
        minm = min(nums)

        res = maxm - minm - 2 * k
        if res < 0:
            res = 0
        return res


nums = [1]; k = 0
nums = [0,10]; k = 2
s = Solution()
print(s.smallestRangeI(nums, k))
