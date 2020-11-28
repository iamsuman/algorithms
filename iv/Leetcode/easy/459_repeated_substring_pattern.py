class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, int(n / 2 + 1)):
            sub_s = s[0:i]
            # print(sub_s * int(n/i))
            if s == sub_s * int(n / i):
                return True
        return False


s = "abab"
s = "aba"
s = "abcabcabcabc"
s = "aaa"
sol = Solution()
print(sol.repeatedSubstringPattern(s))
