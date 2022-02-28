class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def get_gcd(str1):
            res = []
            n = len(str1)
            for i in range(n // 2 + 1):
                # print(i)
                # print(str1[:i+1])
                if str1.replace(str1[:i+1], "") == "":
                    res.append(str1[:i+1])
            res.append(str1)
            return res

        res1 = get_gcd(str1)
        res2 = get_gcd(str2)
        res = ""
        for r in res1:
            if r in res2 and len(r) > len(res):
                res = r
        return res

    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        i = n = len(str1)
        l = len(str2)
        while (i > 0):
            c1 = str1.count(str1[:i])
            if (c1 * (i) == n):
                c1 = str2.count(str1[:i])
                if (c1 * (i) == l):
                    return str1[:i]
            i -= 1

        return ""


str1 = "ABCABC"; str2 = "ABC"
str1 = "ABABAB"; str2 = "ABAB"
str1 = "LEET"; str2 = "CODE"
str1 = "ABABA"; str2 = "ABA"
str1 = "A"; str2 = "ABA"
s = Solution()
print(s.gcdOfStrings(str1, str2))
print(s.gcdOfStrings2(str1, str2))
