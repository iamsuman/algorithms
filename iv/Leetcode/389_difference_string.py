class Solution():
    def find_difference(self, s: str, t: str):
        hash1 = {}
        for i in s:
            if hash1.get(i):
                hash1[i] += 1
            else:
                hash1[i] = 1

        for i in t:
            if hash1.get(i):
                hash1[i] -= 1
            else:
                return i

        for i in hash1:
            if hash1[i] != 0:
                return i


s = "abcd"; t = "abcde"
s = ""; t = "y"
sol = Solution()
print(sol.find_difference(s, t))


