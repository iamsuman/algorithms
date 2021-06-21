from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left = 0
        right = n - 1
        for i in range(n-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                num = nums[left]
                left += 1
            else:
                num = nums[right]
                right -= 1
            res[i] = num * num
        return res

    def sortedSquares1(self, nums: List[int]) -> List[int]:
        nums = list(map(lambda x: x** 2, nums))
        nums.sort()
        return nums

    def sortedSquares2(self, nums: List[int]) -> List[int]:
        return sorted([x*x for x in nums])


nums = [-4,-1,0,3,10]
s = Solution()
print(s.sortedSquares(nums))
print(s.sortedSquares2(nums))
print(s.sortedSquares3(nums))
