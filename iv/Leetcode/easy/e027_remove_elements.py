from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums) - 1
        while i <= n:
            if nums[i] != val:
                i += 1
            else:
                if nums[n] != val:
                    nums[i] = nums[n]
                    i += 1
                n -= 1
        return i

    def removeElement2(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == "__main__":
    nums = [3,2,2,3]; val = 3
    nums = [0, 1, 2, 2, 3, 0, 4, 2]; val = 2
    nums = [0]; val = 0
    nums = [0]; val = 1

    s = Solution()
    print(s.removeElement(nums, val))
    # print(s.removeElement2(nums, val))

