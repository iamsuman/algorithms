class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        def ispalindrome(s: str):
            i = 0
            j = len(s) - 1
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return ispalindrome(s[i:j]) or ispalindrome(s[i+1:j+1])

        return True

    def validPalindrome2(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        count = 0

        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if s[i + 1] == s[j]:
                    count += 1
                    i += 2
                    j -= 1
                    if count > 1:
                        return False
                    continue
                elif s[i] == s[j - 1]:
                    count += 1
                    j -= 2
                    i += 1
                    if count > 1:
                        return False
                    continue
                else:
                    return False

        return True


s = "aba"
s = "abba"
# s = ""
# s = "ab"
# s = "abca"
s = "cbbcc"
s = "abcdefedcuba"
# s = "abcudefedcba"
s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
s = "aguokepatgbnvfqmgmlucupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuclmgmqfvnbgtapekouga"
s = "eeccccbebaeeabebccceea"
s = "eecccbebaeeabebccccee"

sol = Solution()
print(sol.validPalindrome(s))
print(sol.validPalindrome2(s))


