class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        m = len(A)
        n = len(B)
        if m != n:
            return False
        elif m == 0:
            return True

        for i in range(m-1):
            A = A[1:] + A[0]
            if A == B:
                return True
        return False

    def rotateString2(self, A, B):
        return len(A) == len(B) and B in A + A


A = 'abcde'; B = 'cdeab'
# A = "gcmbf"; B = "fgcmb"
# A = "kifcqeiqoh"; B = "ayyrddojpq"
# A = "bbbacddceeb"; B = "ceebbbbacdd"

s = Solution()
print(s.rotateString(A, B))
