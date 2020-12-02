class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i + k] = reversed(a[i:i + k])
        return "".join(a)

    def reverseStr2(self, s: str, k: int) -> str:
        i = 0
        n = len(s)
        res = ""
        while i < n:
            stemp = s[i:i+k]
            res = res + stemp[::-1]
            i = i + k

            s2 = s[i:i+k]
            res = res + s2

            i = i + k
        return res


s = "abcdefg"; k = 2
s = "abcdefg"; k = 5
sol = Solution()
print(sol.reverseStr(s, k))
print(sol.reverseStr2(s, k))


