"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        if m != n:
            return False
        hash1 = {}
        hash2 = {}
        for i in s:
            if hash1.get(i):
                hash1[i] += 1
            else:
                hash1[i] = 1

        for j in t:
            if hash2.get(j):
                hash2[j] += 1
            else:
                hash2[j] = 1

        if hash1 == hash2:
            return True
        else:
            return False


s = "anagram"
t = "nagaram"

# s = "rat"; t = "car"

s = "aacc"
t = "ccac"
sol = Solution()
print(sol.isAnagram(s, t))
