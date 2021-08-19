from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        n = len(nums) // 2
        for i in d.keys():
            if d[i] > n:
                return i
        return None


nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
nums = [1]
s = Solution()
print(s.majorityElement(nums))
