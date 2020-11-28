class Solution:
    def constructRectangle(self, area: int) -> list:
        res = []
        index_diff = 2 ** 31 - 1
        for i in range(1, int(area / 2 + 1) + 1):
            if area % i == 0:
                j = int(area / i)
                if abs(i - j) <= index_diff:
                    index_diff = abs(i - j)
                    if i > j:
                        res = [i, j]
                    else:
                        res = [j, i]
        return res

    def constructRectangle2(self, area: int) -> list:
        arr = []
        for i in range(1, int(area/2 + 1) + 1):
            if area % i == 0:
                j = int(area/i)
                if i > j:
                    arr.append([i,j])
                else:
                    arr.append([j,i])

        min_diff = 2 ** 31 - 1
        index_diff = 0
        for i in range(len(arr)):
            x, y = arr[i]
            if abs(x - y) <= min_diff:
                min_diff = abs(x - y)
                index_diff = i
        return arr[index_diff]


area = 4
# area = 37
# area = 1
area = 122122
s = Solution()
print(s.constructRectangle(area))

