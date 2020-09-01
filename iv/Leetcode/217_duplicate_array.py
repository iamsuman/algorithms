"""
Given an array of integers, find if the array contains any duplicates.
"""
class Solution():
    def contains_duplicates(self, nums):
        if len(nums) < 2:
            return False
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

A = [1,2,3,1]
A = [1,2,3,4]

s = Solution()
print(s.contains_duplicates(A))

