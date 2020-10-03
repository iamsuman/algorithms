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


ransomNote = "a"; magazine = "b"
ransomNote = "aa"; magazine = "aab"
s = Solution()
print(s.canConstruct(ransomNote, magazine))


