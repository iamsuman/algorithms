from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        summ = sum(arr)
        if summ % 3 != 0:
            return False
        tsum = summ / 3


        part1 = 0
        found1 = False
        part2 = 0
        found2 = False
        part3 = 0
        found3 = False
        summ = 0
        for i in range(len(arr)):
            if not found1:
                part1 += arr[i]
                if part1 == tsum:
                    found1 = True
            elif not found2:
                part2 += arr[i]
                if part2 == tsum:
                    found2 = True
            else:
                part3 += arr[i]
                if part3 == tsum:
                    found3 = True
        print(i, tsum, found1, found2, found3)
        if i == (len(arr) -1) and found1 and found2 and found3:
            return True
        else:
            return False


arr = [0,2,1,-6,6,-7,9,1,2,0,1]
arr = [0,2,1,-6,6,7,9,-1,2,0,1]
arr = [3,3,-6, 6, 6,5,-2,2,5,1,-9,4]
arr = [1,1,1,1]

s = Solution()
print(s.canThreePartsEqualSum(arr))





