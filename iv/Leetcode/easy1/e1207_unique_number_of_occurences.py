from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for num in arr:
            d[num] = d.get(num,0) + 1
        vals = d.values()
        print(vals)
        if len(vals) == len(set(vals)):
            return True
        else:
            return False


arr = [1,2,2,1,1,3]
arr = [1,2]
s = Solution()
print(s.uniqueOccurrences(arr))
