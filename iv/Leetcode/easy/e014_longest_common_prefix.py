from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = len(strs)
        n = len(strs[0])
        for i in range(m):
            if len(strs[i]) < n:
                n = len(strs[i])

        res = ""
        for i in range(n):
            ch = strs[0][i]
            prefix = True
            for j in range(1, m):
                if ch != strs[j][i]:
                    prefix = False
                    break
            if prefix:
                res += ch
            else:
                break
        return res


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    strs = ["dog", "racecar", "car"]
    strs = ["cir", "car"]
    strs = ["cir", "car", ""]
    s = Solution()
    print(s.longestCommonPrefix(strs))







