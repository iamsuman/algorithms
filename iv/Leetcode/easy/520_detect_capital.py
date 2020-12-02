import re
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        res = []
        _len = len(word)
        for s in range(_len):
            if word[s].islower():
                res.append(0)
            else:
                res.append(1)

        summ = sum(res)
        if res[0] == 0:
            if summ == 0:
                # AllSmall
                return True
            else:
                return False
        else:
            if summ == 1:
                # cap and all small
                return True
            elif summ == _len:
                # All Caps
                return True
            else:
                return False

    def detectCapitalUse2(self, word: str) -> bool:
        x =  re.fullmatch(r"[A-Z]*|.[a-z]*", word)
        return x


word = "USA"
word = "FlaG"
word = "leetcode"
word = "Google"
sol = Solution()
print(sol.detectCapitalUse(word))
print(sol.detectCapitalUse2(word))










