class Solution():
    def minmoves(self, nums: list) -> int:
        steps = 0
        min_num = min(nums)
        for num in nums:
            steps += abs(min_num - num)
        return steps

    def minmoves(self, nums: list) -> int:
        max_element = max(nums)
        res = 0
        for i in range(len(nums)):
            if i == 0:
                res += max_element - nums[i]
            else:
                if nums[i] != nums[i - 1]:
                    res += max_element - nums[i]
        res = res + nums.count(max_element) - 1
        return res


nums = [1, 2, 3]
nums = [2, 3, 3, 4]
# 3,4,3,5
# 4,4,4
# nums = [1, 1, 2147483647]
s = Solution()
print(s.minmoves(nums))
