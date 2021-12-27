from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums) and k > 0:
            if i+1 == len(nums) or nums[i] <= nums[i+1]:
                nums[i] = -nums[i]
                k -= 1
            else:
                i += 1
                print(nums)
        return sum(nums)

    def largestSumAfterKNegations2(self, nums: List[int], k: int) -> int:

        def get_min(arr: List[int]):
            mina = max(arr)
            ind = 0
            for i in range(len(arr)):
                if arr[i] < mina:
                    mina = arr[i]
                    ind = i
            return ind

        while k > 0:
            i = get_min(nums)
            nums[i] = -1 * nums[i]
            k -= 1
            # print(nums)

        return sum(nums)


nums = [4,2,3]; k = 1
nums = [3,-1,0,2]; k = 3
nums = [2,-3,-1,5,-4]; k = 2
nums = [-2,5,0,2,-2]; k = 3

s = Solution()
print(s.largestSumAfterKNegations(nums, k))
print(s.largestSumAfterKNegations2(nums, k))



