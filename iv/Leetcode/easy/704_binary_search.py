class Solution:
    def search(self, nums: list, target: int) -> int:
        low =0
        hi = len(nums) - 1
        while low <= hi:
            mid = int((low + hi)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                low = mid + 1

        return -1


nums = [-1,0,3,5,9,12]; target = 9
nums = [-1,0,3,5,9,12]; target = 2
s = Solution()
print(s.search(nums, target))

