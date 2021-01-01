class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        subsets = self.find_subsets(A)
        # print(subsets)
        myhash = []
        for arr in subsets:
            p = self.get_products(arr)
            if p in myhash:
                return 0
            else:
                myhash.append(p)
            # print(myhash)
        return 1

    def find_subsets(self, A):
        A = list(str(A))
        res = []
        for i in (range(1, len(A) + 1)):
            for j in (range(len(A))):
                if j + i < len(A) + 1:
                    res.append((A[j:j+i]))
        return res

    def get_products(self, arr):
        prod = 1
        for i in arr:
            prod = prod * int(i)
        return prod


# A = 1234
A = 23
A = 263
s = Solution()
print(s.colorful(A))





