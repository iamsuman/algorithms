from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if d.get(i):
                return i
            else:
                d[i] = 1


nums = [1,2,3,3]
nums = [2,1,2,5,3,2]
s = Solution()
print(s.repeatedNTimes(nums))
