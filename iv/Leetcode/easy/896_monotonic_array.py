from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True

        increasing = 0
        for i in range(len(A) - 1):
            if A[i] == A[i + 1]:
                continue
            elif A[i] < A[i + 1]:
                if increasing == 0:
                    increasing = 1
                elif increasing == -1:
                    return False
            else:
                if increasing == 0:
                    increasing = -1
                elif increasing == 1:
                    return False
        return True


A = [1,2,2,3]
A = [6,5,4,4]
A = [1,3,2]
A = [1,2,4,5]
A = [1,1,1]
s = Solution()
print(s.isMonotonic(A))
