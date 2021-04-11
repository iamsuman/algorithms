from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        pixels = {}
        for i in range(26):
            al = chr(97 + i)
            pixels[al] = widths[i]

        ans = 0
        summ = 0
        m = len(s)
        for i in range(m):
            if 100 - summ  >= pixels[s[i]]:
                if ans == 0:
                    ans += 1
                summ += pixels[s[i]]
            else:
                summ = pixels[s[i]]
                ans += 1
        return [ans, summ]


widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]; s = "abcdefghijklmnopqrstuvwxyz"
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]; s = "bbbcccdddaaa"
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]; s = ""
sol = Solution()
print(sol.numberOfLines(widths,s))







