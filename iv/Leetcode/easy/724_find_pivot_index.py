class Solution:
    def pivotIndex(self, nums: list) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 1
        left_sum = 0
        right_sum = sum(nums) - nums[0]
        for i in range(len(nums)):
            if i != 0:
                left_sum = left_sum + nums[i-1]
                right_sum = right_sum - nums[i]
            if left_sum == right_sum:
                return i
        return -1


nums = [1,7,3,6,5,6]
nums = [1,2,3]
nums = [2,1,-1]
s = Solution()
print(s.pivotIndex(nums))

