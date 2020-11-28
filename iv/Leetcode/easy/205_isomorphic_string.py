"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        target = []
        for i in range(len(s)):
            if dict.get(s[i]):
                if t[i] != dict[s[i]]:
                    return False
            else:
                if t[i] in dict.values():
                    return False
                dict[s[i]] = t[i]

        return True


s = "egg"
t = "add"

s = "ab"
t = "aa"

sl = Solution()
print(sl.isIsomorphic(s,t))



