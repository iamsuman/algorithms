from typing import List
import math


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:

        lo, hi = 0, len(arr) - 1
        res = math.inf
        while lo <= hi:
            mid = int((lo + hi) / 2)
            if arr[mid] == mid:
                if mid < res:
                    res = mid
                hi = (mid - 1)
            elif arr[mid] > mid:
                hi = (mid - 1)
            else:
                lo = mid + 1
        if res == math.inf:
            return -1
        else:
            return res


arr = [-10,-5,0,3,7]
arr = [0,2,5,8,17]
arr = [-10,-5,3,4,7,9]
arr = [-10,-5,-2,0,4,5,6,7,8,9,10]
s = Solution()
print(s.fixedPoint(arr))
