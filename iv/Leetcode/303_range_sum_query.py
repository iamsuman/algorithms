"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
"""


class NumArray:

    def __init__(self, nums: list):
        self.nums = nums
        c_sum = 0
        self.csumm_array = [0] * (len(self.nums) + 1)
        for i in range(len(self.nums)):
            c_sum += self.nums[i]
            self.csumm_array[i+1] = c_sum
        print(self.csumm_array)

    def sumRange(self, i: int, j: int) -> int:
        return self.csumm_array[j+1] - self.csumm_array[i]

    def sumRange2(self, i: int, j: int) -> int:
        summ = 0
        for ii in range(i, j + 1):
            summ += self.nums[ii]
        return summ

nums = [-2, 0, 3, -5, 2, -1]
s = NumArray(nums)
print(s.sumRange(0,2))
print(s.sumRange(2,5))
