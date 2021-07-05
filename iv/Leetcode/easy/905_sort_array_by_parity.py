from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start = 0
        i = 0
        while i < len(A):
            if A[i] % 2 == 0:
                A[start], A[i] = A[i], A[start]
                i += 1
                start += 1
            else:
                i += 1
        return A


A = [3, 1, 2, 4]
A = [2]
s = Solution()
print(s.sortArrayByParity(A))
