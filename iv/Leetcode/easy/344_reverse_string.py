class Solution:
    def reverseString(self, s: list) -> None:
        start = 0
        end = len(s) - 1

        while start < end:
            s[start], s[end] = s[end], s[start]
            start = start + 1
            end = end - 1


s = ["h","e","l","l","o"]
sol = Solution()
sol.reverseString(s)
print(s)
