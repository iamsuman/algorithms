class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 0
        end = num

        while start <= end:
            mid = start + int((end - start) / 2)
            if mid * mid == num:
                # print(mid)
                return True
            elif mid * mid > num:
                end = mid - 1
            else:
                start = mid + 1
        return False


num = 16
num = 2

# num = 1
s = Solution()
print(s.isPerfectSquare(num))
