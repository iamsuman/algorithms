from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [-1] * n
        ind = []
        for i in range(n):
            if s[i] == c:
                answer[i] = 0
                ind.append(i)
        for i in range(n):
            minval = n
            if answer[i] == -1:
                for j in ind:
                    if abs(i-j) < minval:
                        minval = abs(i-j)
                answer[i] = minval
        return answer


s = "loveleetcode"; c = "e"
s = "aaab"; c = "b"
sol = Solution()
print(sol.shortestToChar(s,c))
