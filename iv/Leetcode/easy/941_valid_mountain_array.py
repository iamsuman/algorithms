from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        pivot = -1
        for i in range(1, len(arr) -1):
            if arr[i-1] < arr[i] > arr[i+1]:
                pivot = i
                break
        if pivot == -1:
            return False

        # Strictly Increasing
        for i in range(pivot):
            if arr[i] >= arr[i+1]:
                return False

        # Strictly Decreasing
        for i in range(pivot, len(arr) -1):
            if arr[i] <= arr[i+1]:
                return False

        return True


arr = [2,1]
arr = [3,5,5]
arr = [0,3,2,1]
arr = [0,3,5,3,2,1]
s = Solution()
print(s.validMountainArray(arr))




