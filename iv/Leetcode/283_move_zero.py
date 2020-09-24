"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""
class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastfound = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastfound] = nums[i]
                lastfound += 1
                continue
        for i in range(lastfound, len(nums)):
            nums[i] = 0



    def moveZeroes2(self, nums: list) -> None:
        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            for j in range(i + 1, len(nums)):
                if nums[j] == 0:
                    continue
                nums[i], nums[j] = nums[j], nums[i]
                break


nums = [0,1,0,3,12]
s = Solution()
s.moveZeroes(nums)
print(nums)



