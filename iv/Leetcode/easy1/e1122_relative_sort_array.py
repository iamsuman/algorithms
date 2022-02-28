from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        inclusive = {}
        exclusive = {}
        for num in arr1:
            if num in arr2:
                inclusive[num] = inclusive.get(num, 0) + 1
            else:
                exclusive[num] = exclusive.get(num, 0) + 1

        res = []
        for num in arr2:
            res.extend([num] * inclusive[num])

        for num in sorted(exclusive.keys()):
            res.extend([num] * exclusive[num])

        return res


arr1 = [2,3,1,3,2,4,6,7,9,2,19]; arr2 = [2,1,4,3,9,6]
arr1 = [28,6,22,8,44,17]; arr2 = [22,28,8,6]
arr1 = [2, 4, 0, 3, 2, 3]; arr2 = [2, 0, 3]
s = Solution()
print(s.relativeSortArray(arr1, arr2))
