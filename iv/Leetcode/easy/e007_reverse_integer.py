class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        res = ""
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            res = res + str(x%10)
            x = x // 10
        res_i = int("".join(res))
        if res_i > (2 ** 31 - 1) or res_i < (-2 ** 31):
            return 0
        else:
            return res_i * sign


if __name__ == "__main__":
    x = 32
    x = 2 ** 31
    x = -123
    x = 120
    x = 0
    print(x)
    s = Solution()
    print(s.reverse(x))
