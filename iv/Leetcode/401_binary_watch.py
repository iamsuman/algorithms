class Solution:
    def readBinaryWatch(self, num: int) -> list:
        res = []
        for i in range(0, 12):
            for j in range(0, 60):
                if (bin(i).count('1') + bin(j).count('1')) == num:
                    res.append('%d:%02d' % (i, j))
        return res


n = 1
s = Solution()
print(s.readBinaryWatch(n))
