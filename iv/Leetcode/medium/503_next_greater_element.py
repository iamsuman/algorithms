from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums
        res = [None] * n
        for i in range(n):
            found = False
            for j in range(i+1, i+n):
                if nums[j] > nums[i]:
                    res[i] = nums[j]
                    found = True
                    break
            if not found:
                res[i] = -1
        return res


nums = [1,2,1]
nums = [1,2,3,4,3]
nums = [1]
s = Solution()
print(s.nextGreaterElements(nums))




