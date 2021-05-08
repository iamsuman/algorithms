from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a = sum(A)
        sum_b = sum(B)

        for x in A:
            # Complement
            y = x + int((sum_b - sum_a)/ 2)
            if y in B:
                return [x, y]

    def fairCandySwap2(self, A: List[int], B: List[int]) -> List[int]:
        sum_a = sum(A)
        sum_b = sum(B)
        avg = int((sum_a + sum_b) / 2)

        for i in range(len(A)):
            for j in range(len(B)):
                if sum_a - A[i] + B[j] == avg:
                    return [A[i], B[j]]


A = [1,1]; B = [2,2]
A = [1,2]; B = [2,3]
A = [2]; B = [1,3]
A = [1, 2, 5]; B = [2, 4]
s = Solution()
print(s.fairCandySwap(A,B))
print(s.fairCandySwap2(A,B))
