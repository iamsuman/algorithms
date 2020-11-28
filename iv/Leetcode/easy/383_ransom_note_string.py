class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashset = {}

        for i in ransomNote:
            if hashset.get(i):
                hashset[i] += 1
            else:
                hashset[i] = 1

        for i in magazine:
            if hashset.get(i):
                hashset[i] -= 1

        for i in hashset:
            if hashset[i] != 0:
                return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        # This is slower as hashset grows

        hashset = {}

        for i in magazine:
            if hashset.get(i):
                hashset[i] += 1
            else:
                hashset[i] = 1

        for i in ransomNote:
            if hashset.get(i):
                hashset[i] -= 1
            else:
                return False
        return True


ransomNote = "a"; magazine = "b"
ransomNote = "aa"; magazine = "aab"
ransomNote = "aaaa"; magazine = "aaab"

s = Solution()
print(s.canConstruct2(ransomNote, magazine))


