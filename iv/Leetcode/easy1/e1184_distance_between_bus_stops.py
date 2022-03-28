from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(start, destination), max(start, destination)
        summ = sum(distance)

        d1 = sum(distance[start:destination])
        return min(d1, summ - d1)


distance = [1,2,3,4]; start = 0; destination = 1
distance = [1,2,3,4]; start = 0; destination = 2
distance = [1,2,3,4]; start = 0; destination = 3
s = Solution()
print(s.distanceBetweenBusStops(distance, start, destination))
