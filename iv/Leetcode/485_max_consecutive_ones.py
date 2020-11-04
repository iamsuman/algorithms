class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        max_ones = 0
        streak = 0
        for i in nums:
            if i == 1:
                streak += 1
                if streak > max_ones:
                    max_ones = streak
            else:
                streak = 0
        return max_ones


nums = [1, 1, 0, 1, 1, 1]
s = Solution()
print(s.findMaxConsecutiveOnes(nums))
