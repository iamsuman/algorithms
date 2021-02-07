class Solution:
    def findMaxAverage(self, nums: list, k: int) -> float:
        i = 0
        summ = sum(nums[0:k])
        max_summ = summ
        i += 1
        while i + k - 1 < len(nums):
            summ = summ - nums[i-1] + nums[i + k -1]
            if max_summ < summ:
                max_summ = summ
            i += 1

        return max_summ / k


nums = [1,12,-5,-6,50,3]; k = 4
nums = []; k = 1
s = Solution()
print(s.findMaxAverage(nums, k))


