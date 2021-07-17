from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = int((lo + hi) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        if target > nums[lo]:
            return lo + 1
        else:
            return lo


nums = [1,3,5,6]; target = 5
nums = [1,3,5,6]; target = 2
nums = [1,3,5,6]; target = 7
nums = [1,3,5,6]; target = 0
nums = [1]; target = 0
s = Solution()
print(s.searchInsert(nums, target))



