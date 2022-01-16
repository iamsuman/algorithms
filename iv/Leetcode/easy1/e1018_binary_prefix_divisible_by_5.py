from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0
        res = []
        for i in range(len(nums)):
            num = num * 2 + nums[i]
            # print(num)
            # if num % 5 == 0:
            #     res.append(True)
            # else:
            #     res.append(False)
            res.append(num % 5 == 0)
        return res


nums = [0,1,1]
nums = [1,1,1]
s = Solution()
print(s.prefixesDivBy5(nums))

