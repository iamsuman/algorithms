"""
Given a string, find the length of the longest substring without repeating characters.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        i = 0
        j = 0
        res = 0
        while i < len(s):
            myhash = []
            while j < len(s):
                if s[j] in myhash:
                    if len(myhash) > res:
                        res = len(myhash)
                    if myhash: myhash.pop(0)
                    i = i + 1
                else:
                    myhash.append(s[j])
                    j = j + 1
            if len(myhash) > res:
                res = len(myhash)
            i = i + 1
            if myhash: myhash.pop(0)

        return res

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        Time Complexity: O(n ** 2)
        Space Complexity: O(1)
        """
        res = 0
        for i in range(len(s)):
            myhash = []
            j = i
            while j < len(s):
                if s[j] in myhash:
                    break
                else:
                    myhash.append(s[j])
                j = j + 1
            if len(myhash) > res:
                res = len(myhash)
        return res


A = "abcabcbb"
ans = 3
s = Solution()
print(s.lengthOfLongestSubstring(A))
if s.lengthOfLongestSubstring(A) == ans:
    print("Test Passed")


