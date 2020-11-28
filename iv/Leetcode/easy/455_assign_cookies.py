class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        if len(s) == 0:
            return 0
        g.sort(reverse=True)
        s.sort(reverse=True)

        i = 0
        ans = 0
        for child in g:
            if s[i] >= child:
                ans += 1
                i += 1
            if i >= len(s):
                break
        return ans


g = [1, 2];
s = [1, 2, 3]
g = [1, 2, 3];
s = [1, 1]
g = [1, 2, 3];
s = []
sol = Solution()
print(sol.findContentChildren(g, s))
