class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        sl = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if sl[i].isalpha():
                if sl[j].isalpha():
                    sl[i], sl[j] = sl[j], sl[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1
        return "".join(sl)


s = "ab-cd"
s = "a-bC-dEf-ghIj"
s = "Test1ng-Leet=code-Q!"
sol = Solution()
print(sol.reverseOnlyLetters(s))
