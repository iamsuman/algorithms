from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        for c in chars:
            d[c] = d.get(c, 0) + 1
        r = {}
        res = []
        for word in words:
            r = {}
            for c in word:
                r[c] = r.get(c, 0) + 1
            formation = True
            for k in r.keys():
                if not (k in chars and r[k] <= d[k]):
                    formation = False
                    break
            if formation:
                res.append(word)
        # print(res)
        summ = 0
        for word in res:
            summ += len(word)
        return summ


words = ["cat","bt","hat","tree"]; chars = "atach"
words = ["hello","world","leetcode"]; chars = "welldonehoneyr"
words = ["h"]; chars = "a"
s = Solution()
print(s.countCharacters(words, chars))




