"""
A student could be rewarded if his attendance record doesn't contain
more than one 'A' (absent) or more than two continuous 'L' (late).
"""
class Solution:
    def checkRecord(self, s: str):
        a_count = 0
        l_count = 0
        for a in s:
            if a == "A":
                a_count += 1
                l_count = 0
            elif a == "L":
                l_count += 1
            else:
                l_count = 0
            if a_count > 1 or l_count > 2:
                return False
        return True


s = "PPALLP"
s = "PPALLL"
s = "LPLPLPLPLPL"
sol = Solution()
print(sol.checkRecord(s))




