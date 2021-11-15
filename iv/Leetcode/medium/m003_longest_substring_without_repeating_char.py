class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        res = 0
        for i in range(len(s)):
            if s[i] in arr:
                res = max(res, len(arr))
                arr.append(s[i])
                ind = arr.index(s[i])
                arr = arr[ind+1:]
            else:
                arr.append(s[i])
                res = max(res, len(arr))
        return res


s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
s = ""
s = "aab"

sol = Solution()
print(sol.lengthOfLongestSubstring(s))
