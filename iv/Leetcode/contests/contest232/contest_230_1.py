class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        same = 0
        dif = 0
        ind = []
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                same += 1
            else:
                dif += 1
                if dif > 2:
                    return False
                ind.append(i)

        if dif == 1:
            return False
        if dif == 0:
            return True
        if s1[ind[0]] != s2[ind[1]]:
            return False
        return True

s1 = "bank"; s2 = "kanb"
s1 = "attack"; s2 = "defend"
s1 = "kelb"; s2 = "kelb"
s1 = "abcd"; s2 = "dcba"
s1 = "a"; s2="b"
s1= "ab"; s2="ac"
s1 = "abc"; s2="bac"
s1 = "abc"; s2="aba"
s = Solution()
print(s.areAlmostEqual(s1,s2))

