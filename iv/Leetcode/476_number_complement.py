class Solution:
    def findComplement(self, num: int) -> int:
        # TODO binary
        x = bin(num)[2:]
        y = "1" * len(x)
        return int(x, 2) ^ int(y, 2)

    def findComplement(self, num: int) -> int:
        bin_num = self.binary(num)
        bin_comp = ""
        for s in bin_num:
            if s == "0":
                c = "1"
            else:
                c = "0"
            bin_comp = bin_comp + c
        dec_num = self.dec(bin_comp)
        return dec_num

    def binary(self, num: int):
        res = ""
        if num == 0:
            return "0"
        while num > 0:
            res = str(num % 2) + res
            num = int(num / 2)
        return res

    def dec(self, bin_num: str):
        res = 0
        for i in bin_num:
            res = res * 2 + int(i)
        return res


num = 5
# num = 1
s = Solution()
# print(s.binary(10))
# print(s.dec("1010"))
print(s.findComplement(num))
