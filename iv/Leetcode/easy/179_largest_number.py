"""
Given a list of non negative integers, arrange them such that they form the largest number.
"""
class LargerNumber(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution(object):
    def largestNumber(self, nums):
        """
        Time Complexity: O(nlog(n))
        Space Complexity: O(1)
        """
        nums = list(map(str, nums))
        nums = sorted(nums, key=LargerNumber)
        while len(nums) > 1:
            if nums[0] == "0":
                nums.pop(0)
            else:
                break
        return "".join(nums)

    def largestNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        Time Complexity: O(n**2)
        Space Complexity: O(1)
        """
        nums = list(map(str, nums))
        for i in range(len(nums)):
            j = 0
            while j < len(nums) - i - 1:
                nums[j], nums[j + 1] = self.sort_number(nums[j], nums[j + 1])
                j += 1
        while len(nums) > 1:
            if nums[0] == "0":
                nums.pop(0)
            else:
                break
        return "".join(nums)

    def sort_number(self, a, b):
        if int(a + b) > int(b + a):
            return a, b
        else:
            return b, a


A = [10,2]

A = [3,30,34,5,9]
ans = "9534330"

A = [0,0,0]
ans = "0"
s = Solution()
print(s.largestNumber(A))
if s.largestNumber(A) == ans:
    print("Success")

