class Solution():
    # @param A : string
    # @return an integer
    def power(self, A):
        A = int(A)
        if A == 0 or A == 1:
            return 0
        else:
            return self.ispoweroftwo(A)

    def ispoweroftwo(self, n):
        while (n != 1):
            if (n % 2 != 0):
                return 0
            n = n // 2
        return 1

s = Solution()
A = 128
A = 66
A = 2 ** 64
# A = 1
# A = 0
# A = "2"
print(s.power(A))
