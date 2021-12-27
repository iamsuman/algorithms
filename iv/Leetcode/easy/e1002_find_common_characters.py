from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = {}
        for s in words[0]:
            d[s] = d.get(s, 0) + 1

        for word in words[1:]:
            for s in list(d.keys()):
                if word.count(s) == 0:
                    d.pop(s)
                elif word.count(s) < d[s]:
                    d[s] = word.count(s)
        res = []
        for s in list(d.keys()):
            res.extend([s] * d[s])
        return res


words = ["bella","label","roller"]
sol = Solution()
print(sol.commonChars(words))



