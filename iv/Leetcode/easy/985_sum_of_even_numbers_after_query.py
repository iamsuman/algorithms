from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        summ = sum([x for x in nums if x%2 == 0])
        for i in range(n):
            val = queries[i][0]
            index = queries[i][1]
            if nums[index] % 2 == 0 and val % 2 == 0:
                summ += val
            elif nums[index] % 2 == 0 and val % 2 != 0:
                summ -= nums[index]
            elif nums[index] % 2 != 0 and val % 2 != 0:
                summ += (val + nums[index])
            nums[index] += val
            answer[i] = summ
        return answer

    def sumEvenAfterQueries2(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        for i in range(n):
            val = queries[i][0]
            index = queries[i][1]
            nums[index] += val
            answer[i] = sum([x for x in nums if x%2 == 0])
        return answer


nums = [1,2,3,4]; queries = [[1,0],[-3,1],[-4,0],[2,3]]
s = Solution()
print(s.sumEvenAfterQueries(nums,queries))

