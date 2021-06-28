class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i = 0
        num = 0
        while i < len(s)-1:
            if d[s[i]] < d[s[i+1]]:
                num += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                num += d[s[i]]
                i += 1
        if i == len(s)-1:
            num += d[s[i]]
        return num


if __name__ == "__main__":
    s = "III"
    s = "IV"
    s = "IX"
    s = "LVIII"
    s = "MCMXCIV" # 1994
    sol = Solution()
    print(sol.romanToInt(s))



