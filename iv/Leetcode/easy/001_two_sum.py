class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        myhash = {}
        for i in range(len(nums)):
            if myhash.get(nums[i]):
                counter = myhash.get(nums[i])
                return [i, counter[0]]
            else:
                diff = target - nums[i]
                if myhash.get(diff):
                    (myhash.get(diff)).append(i)
                else:
                    myhash[diff] = [i]


# nums = [2,7,11,15]; target = 9
nums = [2,7,7,7,9,11,15]; target = 16
s = Solution()
print(s.twoSum(nums, target))


