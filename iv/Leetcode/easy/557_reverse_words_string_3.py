class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res = []
        for word in words:
            res.append(word[::-1])
        return " ".join(res)


s = "Let's take LeetCode contest"
sol = Solution()
print(sol.reverseWords(s))
