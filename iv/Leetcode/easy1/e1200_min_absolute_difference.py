import math
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = math.inf
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                min_diff = diff
        res = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == min_diff:
                res.append([arr[i], arr[i+1]])
        return res


arr = [4,2,1,3]
# arr = [1,3,6,10,15]
# arr = []
# for i in range(1,100000):
#     arr.append(i)
# print(arr)
s = Solution()
print(s.minimumAbsDifference(arr))


