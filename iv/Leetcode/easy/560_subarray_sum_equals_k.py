"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        dict = {0:1}
        summ = 0
        count = 0
        for i in range(len(nums)):
            summ = summ + nums[i]
            if dict.get(summ):
                dict[summ] += 1
            else:
                dict[summ] = 1
            if summ - k in dict:
                count += dict[summ -k]
        return count


A = [1,1,1]
k = 2
s = Solution()
print(s.subarraySum(A, k))
