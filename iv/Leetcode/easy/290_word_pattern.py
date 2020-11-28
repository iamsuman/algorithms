class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        plen = len(pattern)
        slen = len(s)

        if plen != slen:
            return false

        myhash = {}
        for i in range(len(s)):
            if myhash.get(pattern[i]):
                if myhash[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in myhash.values():
                    return False
                else:
                    myhash[pattern[i]] = s[i]
        return True


pattern = "abba"
s = "dog cat cat dog"

pattern = "abba"
s = "dog cat cat fish"

sol = Solution()
print(sol.wordPattern(pattern, s))

