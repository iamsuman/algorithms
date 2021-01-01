# A = [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1]; B = 3  # 9
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        start = 0
        end = 0
        zeros = 0
        maxcount = 0
        # res = []
        while end < len(A):
            if A[end] == 1:
                if maxcount < end - start + 1:
                    maxcount = end - start + 1
                    # res = list(range(start, end + 1))
                end += 1
            else:
                if zeros < B:
                    if maxcount < end - start + 1:
                        maxcount = end - start + 1
                        # res = list(range(start, end + 1))
                    end += 1
                    zeros += 1
                else:
                    if A[start] == 0:
                        zeros -= 1
                    start += 1
        return maxcount


A = [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1]; B = 3  # 9
s = Solution()
print(s.solve(A, B))
