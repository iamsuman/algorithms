"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j
in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""


class Solution():
    def contains_dups(self, nums, k):
        nhash = {}
        for i in range(len(nums)):
            if nhash.get(nums[i]):
                j = max(nhash[nums[i]])
                if i - j <= k:
                    return True
                nhash[nums[i]].append(i)
            else:
                nhash[nums[i]] = [i]
        return False


nums = [1, 2, 3, 1]
k = 3

# nums = [1, 2, 3, 1, 2, 3]
# k = 2
s = Solution()
print(s.contains_dups(nums, k))
