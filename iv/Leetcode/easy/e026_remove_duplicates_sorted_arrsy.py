from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] > nums[i]:
                nums[i+1] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        # print(nums)
        return i + 1


nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
nums = []
nums = [1]
nums = [1,1]
s = Solution()
print(s.removeDuplicates(nums))


