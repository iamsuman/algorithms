class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i

    def num_to_binary(self, m: int):
        if m == 0:
            return "0"
        res = ""
        while m > 0:
            rem = m % 2
            res = str(rem) + res
            m = m // 2
        return res

    def binary_to_num(self, x: str):
        res = 0
        for i in x:
            res = 2 * res + int(i)
        return res


m = 5; n = 7
m = 0; n = 1
# m = 1; n = 1
# m = 2; n = 1
# m = 6; n = 7
s = Solution()
# print(s.num_to_binary(0))
# print(s.binary_to_num("101"))
print(s.rangeBitwiseAnd(m,n))

