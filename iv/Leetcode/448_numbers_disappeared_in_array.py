class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        for i in range(len(nums)):
            ind = abs(nums[i]) - 1
            if nums[ind] > 0:
                nums[ind] = -1 * nums[ind]
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res

    def findDisappearedNumbers2(self, nums: list) -> list:
        # Time Complexity: O(nlog(n))
        # Space Complexity: O(1)
        if len(nums) == 0:
            return []
        nums.sort()
        res = []
        if nums[0] > 1:
            res.extend(list(range(1, nums[0])))

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                res.extend(list(range(nums[i] + 1, nums[i + 1])))
        if nums[-1] != len(nums):
            res.extend(list(range(nums[-1] + 1, len(nums) + 1)))
        return res


nums = [4, 3, 2, 7, 8, 2, 3, 1]
nums = [1, 2, 2, 3, 4]
nums = []
s = Solution()
print(s.findDisappearedNumbers(nums))
