class Solution:
    def dominantIndex(self, nums: list) -> int:
        max_num = max(nums)
        for i in range(len(nums)):
            if nums[i] != max_num and nums[i] * 2 > max_num:
                return -1
        return nums.index(max_num)


nums = [3, 6, 1, 0]
# nums = [1, 2, 3, 4]
nums = [1]
nums = [2,2]
s = Solution()
print(s.dominantIndex(nums))
