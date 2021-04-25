from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def bin_search(low, hi):
            mid = low + int((hi - low)/2)
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid-1]:
                low = mid
                return bin_search(low, hi)
            elif arr[mid] > arr[mid+1]:
                hi = mid
                return bin_search(low, hi)
        return bin_search(0, len(arr))

    def peakIndexInMountainArray2(self, arr: List[int]) -> int:
        for i in range(1,len(arr) - 1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i


arr = [0,1,0]
arr = [0,2,1,0]
arr = [3,4,5,1]
arr = [24,69,100,99,79,78,67,36,26,19]
arr = [24,69,81,100,99,79,78,67,36,26,19]
s = Solution()
print(s.peakIndexInMountainArray(arr))

