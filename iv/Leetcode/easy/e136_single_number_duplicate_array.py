from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # TODO: solve with XOR
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i]):
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        for i in d.keys():
            if d[i] == 1:
                return i


nums = [2,2,1]
s = Solution()
print(s.singleNumber(nums))
