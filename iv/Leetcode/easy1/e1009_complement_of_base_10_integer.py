class Solution:
    def bitwiseComplement(self, n: int) -> int:
        st = self.get_binary(n)
        com = ""
        for i in range(len(st)):
            if st[i] == "0":
                com += "1"
            else:
                com += "0"
        # print(com)
        return self.get_num(com)

    def get_binary(self, n: int):
        if n == 0:
            return "0"
        res = ""
        while n > 0:
            res = str(n%2) + res
            n = n // 2
        return res

    def get_num(self, st: str):
        res = 0
        for i in range(len(st)):
            res = res * 2 + int(st[i])
        return res


n = 5
s = Solution()
print(s.get_binary(n))
print(s.get_num(s.get_binary(n)))
print(s.bitwiseComplement(n))
