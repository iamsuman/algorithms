class Solution:
    # Dynamic programming: Optimal substructure.
    # TC: O(n), SC: O(2n) - 2 dp arrays
    def rob(self, nums: list) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Case 1 start with h0 - hn-1
        dp1 = [None] * (len(nums) - 1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        # dp is Maximum amount of money On Houses
        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i - 1], nums[i] + dp1[i - 2])

            # Case 2 start with h1 - hn
        dp2 = [None] * (len(nums) - 1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])

        # dp is Maximum amount of money On Houses
        for i in range(2, len(nums) - 1):
            dp2[i] = max(dp2[i - 1], nums[i + 1] + dp2[i - 2])

        return max(dp1[-1], dp2[-1])


nums = [1,2,3,1]
s = Solution()
print(s.rob(nums))
