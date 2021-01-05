class Solution:
    def minSubArrayLen(self, s: int, nums: list) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # TODO Binary Search O(nlog(n))

        if not nums or sum(nums) < s:
            return 0

        min_len = len(nums)
        current_sum = 0
        left = 0
        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= s:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_len


s = 7; nums = [2,3,1,2,4,3]
s = 3; nums = [1,1]
sol = Solution()
print(sol.minSubArrayLen(s, nums))


