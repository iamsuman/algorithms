class Solution:
    def maximumProduct(self, nums: list) -> int:
        nums.sort()
        max_product_1 = nums[-1] * nums[-2] * nums[-3]
        max_product_2 = nums[0] * nums[1] * nums[-1]
        return max(max_product_1, max_product_2)


nums = [1,2,3,4]
nums = [-1,-2,-3]
nums = [-1,-2,-3, 0, 2]
s = Solution()
print(s.maximumProduct(nums))
