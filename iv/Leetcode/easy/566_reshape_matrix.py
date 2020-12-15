class Solution:
    def matrixReshape(self, nums: list, r: int, c: int) -> list:
        rr = len(nums)
        cc = len(nums[0])

        if r * c > rr * cc:
            return nums

        flat = []
        for i in range(rr):
            for j in range(cc):
                flat.append(nums[i][j])

        res = []
        for i in range(r):
            res.append([0] * c)

        k = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = flat[k]
                k = k + 1
        return res


nums = [[1, 2], [3, 4]]
r = 2;
c = 4

r = 1
# nums = [[]]

s = Solution()
print(s.matrixReshape(nums, r, c))
