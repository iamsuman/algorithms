"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashset = {}
        for i in range(len(s)):
            if hashset.get(s[i]):
                hashset[s[i]] += 1
            else:
                hashset[s[i]] = 1

        for i in range(len(s)):
            if hashset[s[i]] == 1:
                return i

        return -1


s = "leetcode"
s = "loveleetcode"
s = ""
sol = Solution()
print(sol.firstUniqChar(s))





