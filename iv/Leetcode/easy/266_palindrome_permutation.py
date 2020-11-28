class Solution():
    def ispalindromeperm(self, s: str):
        myhash = {}
        for i in range(len(s)):
            if myhash.get(s[i]):
                myhash[s[i]] += 1
            else:
                myhash[s[i]] = 1

        if len(s) % 2 == 0:
            odd = False
        else:
            odd = True
        count_odd = 0
        for (a, b) in myhash.items():
            if b % 2 == 1:
                if not odd:
                    return False
                count_odd += 1
            if count_odd > 1:
                return False
        return True


s = "code"
# s = "aab"
s = "carerac"
sol = Solution()
print(sol.ispalindromeperm(s))



