"""
Run length encoding for a string
"""
class Solution():
    def encode(self, A):
        prev = ""
        count = 0
        res = ""
        for i in range(len(A)):
            if A[i] == prev:
                count = count + 1
            else:
                if prev != "":
                    res = res + str(count) + prev
                count = 1
                prev = A[i]
        res = res + str(count) + prev
        return res

    def decode(self, A):
        res = ""
        i =1
        while i < len(A):
            res = res + int(A[i-1]) * A[i]
            i = i + 2
        return res


A = "aabbbcca"
print(A)
s = Solution()
enc = s.encode(A)
print(enc)
dec = s.decode(enc)
print(dec)
if A == dec:
    print("Matches")






