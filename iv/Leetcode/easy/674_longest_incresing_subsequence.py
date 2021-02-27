class Solution:
    def findLengthOfLCIS(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        max_length = 0
        length = 0
        for i in range(len(nums)):
            if i == 0:
                length = 1
            else:
                if nums[i] > nums[i-1]:
                    length += 1
                else:
                    length = 1
            if max_length < length:
                max_length = length

        return max_length


nums = [1,3,5,4,7]
nums = [2,2,2,2,2]
s = Solution()
print(s.findLengthOfLCIS(nums))
