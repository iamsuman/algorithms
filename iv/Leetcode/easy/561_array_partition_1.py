"""
Given an integer array nums of 2n integers, group these integers into
n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized.
Return the maximized sum.
"""


class Solution:
    def arrayPairSum(self, nums: list) -> int:
        nums.sort(reverse=True)
        summ = 0
        for i in range(0, len(nums) - 1, 2):
            # summ += min(nums[i], nums[i +1])
            summ += nums[i + 1]
        return summ

    # TODO HashMap O(n)


nums = [1, 4, 3, 2]
# nums = [6,2,6,5,1,2]
s = Solution()
print(s.arrayPairSum(nums))
