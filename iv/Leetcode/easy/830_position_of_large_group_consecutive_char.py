from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) < 3:
            return []
        res = []
        start = 0
        end = 0
        count = 0
        for i in range(len(s)):
            if i == 0:
                count += 1
                continue
            if s[i] == s[i-1]:
                count += 1
            else:
                if count >= 3:
                    res.append([start, i-1])
                count = 1
                start = i
        if count >= 3:
            res.append([start, i])
        return res


s = "abbxxxxzzy"
s = "abc"
s = "abcdddeeeeaabbbcd"
s = "aba"
s = "aaa"
sol = Solution()
print(sol.largeGroupPositions(s))
