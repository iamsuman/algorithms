import heapq
class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        # if len(nums) == 0:
        #     return 0
        nums.sort(reverse=True)
        return nums[k - 1]

    def findKthLargest2(self, nums: list, k: int):
        heap = []
        for x in nums:
            heapq.heappush(heap, -x)
        for i in range(k - 1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)


nums = [3,2,1,5,6,4]; k = 2
nums = [3,2,3,1,2,4,5,5,6]; k = 4
s = Solution()
print(s.findKthLargest(nums, k))
print(s.findKthLargest2(nums, k))
