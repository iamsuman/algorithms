from typing import List
import math


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        slope = []
        for i in range(len(points)):
            if i == len(points) - 1:
                j = 0
            else:
                j = i + 1
            if (points[j][0] - points[i][0]) == 0:
                slope1 = math.inf
            else:
                slope1 = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
            if slope1 not in slope:
                slope.append(slope1)
            else:
                print(slope, slope1)
                return False
        print(slope)
        return True


points = [[1,1],[2,3],[3,2]]
points = [[1,1],[2,2],[3,3]]
points = [[2,2],[3,3],[1,1]]
s = Solution()
print(s.isBoomerang(points))
