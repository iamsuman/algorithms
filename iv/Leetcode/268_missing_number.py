"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""
class Solution():
    def missingNumber(self, nums: list):
        summ = sum(nums)
        n = len(nums)
        arithmetic_sum = int(n * (n + 1) / 2)
        return arithmetic_sum - summ

    def missingNumber2(self, nums: list):
        # Sorting
        # Time Complexity n * log(n)
        # Space Complexity O(1)

        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return i + 1

    def missingNumber2(self, nums: list):
        for i in range(len(nums)):
            if i in nums:
                continue
            else:
                return i
        return i + 1

num = [3,0,1]
num = [0, 1, 2]
s = Solution()
print(s.missingNumber(num))


