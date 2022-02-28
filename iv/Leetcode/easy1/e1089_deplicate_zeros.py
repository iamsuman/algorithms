from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        summ = 0
        i = 0
        last = True
        while summ < n:
            if arr[i] == 0:
                if n - summ >= 2:
                    summ += 2
                else:
                    last = False
                    summ += 1
            else:
                summ += 1
            i += 1
        right = i - 1
        print(f"{last}, {right}")
        i = n - 1
        while i >= 0:
            if arr[right] == 0:
                if last:
                    arr[i] = arr[right]
                    arr[i - 1] = 0
                    i -= 2
                else:
                    arr[i] = arr[right]
                    last = True
                    i -= 1
            else:
                arr[i] = arr[right]
                i -= 1
            right -= 1


arr = [1,0,2,3,0,4,5,0]
arr = [1,2,3]
arr = [1,0]
arr = [1,0,3]
arr = [1,2,3,0]
arr = [1,0,3,0,4]
arr = [1,5,2,0,6,8,0,6,0]
s = Solution()
print(arr)
s.duplicateZeros(arr)
print(arr)



