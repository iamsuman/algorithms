class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        res = []
        lic = S.replace("-", "")
        remainder = len(lic) % K
        prev = 0
        if remainder > 0:
            res.append(lic[:remainder])
            prev += remainder
        while prev < len(lic):
            res.append(lic[prev: prev + K])
            prev += K
        res = "-".join(res)
        return res.upper()


S = "5F3Z-2e-9-w"; K = 4
S = "2-5g-3-J"; K = 2
S = "aaa"; K = 1
S = "2-4A0r7-4k"; K = 4

s = Solution()
print(s.licenseKeyFormatting(S, K))

