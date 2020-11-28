class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = bin(x ^ y)
        return res.count("1")


x = 1;
y = 4
x = 0;
y = 0
s = Solution()
print(s.hammingDistance(x, y))
