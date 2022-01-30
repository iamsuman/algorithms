from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = [0] * 101
        for h in heights:
           counts[h] += 1

        i = 0
        j = 0
        res = 0
        while i < len(heights):
            while counts[j] == 0:
                j += 1
            while counts[j] > 0:
                if heights[i] != j:
                    res += 1
                i += 1
                counts[j] -= 1
        return res

    def heightChecker2(self, heights: List[int]) -> int:
        h = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != h[i]:
                count += 1
        return count


heights = [1,1,4,2,1,3]
heights = [5,1,2,3,4]
heights = [1,2,3,4,5]
s = Solution()
print(s.heightChecker(heights))
print(s.heightChecker2(heights))
