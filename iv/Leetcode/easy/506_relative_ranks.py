class Solution:
    def findRelativeRanks(self, nums: list) -> list:
        m = max(nums)
        # nums = list(map(lambda x: m - x, nums))
        candidates = (enumerate(nums))
        candidates = sorted(candidates, key=lambda x: x[1], reverse= True)
        res = [""] * len(nums)
        for i in range(len(nums)):
            (j, k) = candidates[i]
            if i == 0:
                val = "Gold Medal"
            elif i == 1:
                val = "Silver Medal"
            elif i == 2:
                val = "Bronze Medal"
            else:
                val = str(i + 1)
            res[j] = val
        return res


nums = [5, 8, 4, 6, 2, 1]
# nums = [1, 2, 5, 3]
s = Solution()
print(s.findRelativeRanks(nums))
