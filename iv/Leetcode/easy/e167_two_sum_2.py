from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            summ = numbers[i] + numbers[j]
            if summ == target:
                return [i + 1, j + 1]
            elif summ > target:
                j -= 1
            else:
                i += 1

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in res.keys():
                return [res[diff]+1, i+1]
            else:
                res[numbers[i]] = i
        return [-1, -1]


numbers = [2, 7, 11, 15]; target = 9
# numbers = [2, 3, 4]; target = 6
# numbers = [-1,0]; target = -1
s = Solution()
print(s.twoSum(numbers, target))
print(s.twoSum2(numbers, target))
