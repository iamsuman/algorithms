class Solution:
    def nextGreaterElement(self, n: int) -> int:
        temp = n
        res = []
        while temp > 0:
            res.append(temp % 10)
            temp = int(temp / 10)
        res = res[::-1]

        maxm = res[-1]
        ind = len(res) - 1
        while ind >= 0:
            if res[ind] < maxm:
                break
            else:
                maxm = res[ind]
                ind -= 1
        if ind < 0:
            return -1

        rev = res[ind+1:]
        minm = max(rev) + 1
        ind1 = -1
        for i in range(len(rev)):
            if rev[i] > res[ind]:
                if minm > rev[i]:
                    minm = rev[i]
                    ind1 = i

        rev[ind1] = res[ind]
        res[ind] = minm

        rev.sort()
        res = res[:ind+1] + rev
        res = list(map(lambda x: str(x), res))
        ans = int("".join(res))
        if ans > 2 ** 31 -1:
            return -1
        return ans


# n = 21
n = 12
n = 12453
# n = 222
# n = 1
n = 2**31 - 1
n = 2147483476
n = 230241
# 2147483647
print(n)
s = Solution()
print(s.nextGreaterElement(n))

