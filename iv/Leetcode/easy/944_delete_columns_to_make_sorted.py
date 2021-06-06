from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        if n == 1:
            return 0
        if m == 1:
            if sorted(strs) == strs:
                return 0
            else:
                return 1

        arr = []
        for i in range(n):
            arr.append([None] * m)
            for j in range(m):
                arr[i][j] = strs[i][j]
        print(arr)

        count = 0
        for j in range(m):
            for i in range(n-1):
                # print(arr[i][j], arr[i+1][j])
                if arr[i][j] > arr[i+1][j]:
                    count += 1
                    break
        return count


strs = ["cba","daf","ghi"]
strs = ["a","b"]
# strs = ["zyx","wvu","tsr"]
strs = ["rrjk","furt","guzm"]
s = Solution()
print(s.minDeletionSize(strs))





