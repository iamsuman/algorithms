class Solution:
    def get_tribonacci(self, n: int) -> int:
        T = {0: 0, 1: 1, 2: 1}
        for i in range(3, n+1):
            T[i] = T[i-3] + T[i-2] + T[i-1]
        return T[n]

    def get_tribonacci2(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n+1)
        nums[1] = 1
        nums[2] = 1

        def helper(n):
            if n == 0:
                return 0
            if nums[n]:
                return nums[n]
            nums[n] = helper(n-1) + helper(n-2) + helper(n-3)
            return nums[n]

        return helper(n)


n = 4
n = 25
# n = 0
s = Solution()
print(s.get_tribonacci(n))
print(s.get_tribonacci2(n))

