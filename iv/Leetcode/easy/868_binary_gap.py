class Solution:
    def binaryGap(self, n: int) -> int:
        bin_n = self.binary(n)

        start = -1
        max_diff = 0
        for i in range(len(bin_n)):
            if bin_n[i] == "1":
                if start != -1:
                    if max_diff < i - start:
                        max_diff = i - start
                start = i
        return max_diff

    def binary(self, n):
        res = ""
        while n > 0:
            res = str(n % 2) + res
            n = int(n/2)
        return res


n = 22
n = 5
n = 6
n = 8
n = 0
s = Solution()
print(s.binary(22))
print(s.binaryGap(n))
