class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)
        s = s[2:]
        if len(s) < 32:
            s = "0" * (32 - len(s)) + s
        print(s)
        return s.count("1")

n = 0b00000000000000000000000000001011
n = 0b00000000000000000000000010000000
n = 0b11111111111111111111111111111101
n = 0b00000000000000000000000000000000
n = 54
s = Solution()
print(s.hammingWeight(n))
