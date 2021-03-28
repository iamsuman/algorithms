class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = []
        for i in range(n):
            perm.append(i)

        def op(perm):
            arr = [0] * len(perm)
            for i in range(len(perm)):
                if i % 2 == 0:
                    arr[i] = perm[int(i / 2)]
                else:
                    arr[i] = perm[int(len(perm) / 2 + (i - 1) / 2)]
            return arr

        count = 0
        arr_list = []
        temp = [0] * n
        for i in range(n):
            temp[i] = perm[i]
        while True:
            arr = op(temp)
            # print(arr, perm)
            count += 1
            if arr == perm:
                return count
            # else:
            #     if arr in arr_list:
            #         return -1
            # arr_list.append(arr)
            for i in range(n):
                temp[i] = arr[i]


n = 2
n = 4
n = 6
n = 8
s = Solution()
print(s.reinitializePermutation(n))
for i in range(2, 1000, 2):
    print(i, s.reinitializePermutation(i))
