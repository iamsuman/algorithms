class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1

        lo, hi = 1, x // 2
        while lo <= hi:
            mid = int((lo + hi) / 2)
            sq = mid * mid
            if sq == x:
                return mid
            elif sq > x:
                hi = mid - 1
            else:
                lo = mid + 1
        return min(lo, hi)


x = 4
x = 10
s = Solution()
for x in range(1, 100):
    print(x, s.mySqrt(x))

