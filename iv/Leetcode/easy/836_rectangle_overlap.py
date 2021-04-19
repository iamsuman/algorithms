from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[2] <= rec2[0] or \
            rec1[3] <= rec2[1] or \
            rec1[0] >= rec2[2] or \
            rec1[1] >= rec2[3]:
            return False
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or
            rec2[0] == rec2[2] or rec2[1] == rec2[3]):
            # the line cannot have positive overlap
            return False

        return True


rec1 = [0, 0, 2, 2];
rec2 = [1, 1, 3, 3]
s = Solution()
print(s.isRectangleOverlap(rec1, rec2))
