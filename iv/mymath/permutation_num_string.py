"""
Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of first n positive integer that satisfy the given input string.

D means the next number is smaller, while I means the next number is greater.
Input 1:
n = 3
s = ID
Return: [1, 3, 2]
"""


class Solution():
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        arr = list(range(1, B + 1))
        res = []
        j = 0
        for i in range(len(A)):
            if A[i] == "D":
                j = j + 1
            else:
                if j > 0:
                    temp = arr[:j + 1]
                    temp.sort(reverse=True)
                    res = res + temp
                    arr = arr[j + 1:]
                    j = 0
                else:
                    res = res + [arr[j]]
                    arr = arr[j + 1:]
        if len(res) <= len(A):
            if j > 0:
                temp = arr[:j + 1]
                temp.sort(reverse=True)
                res = res + temp
                arr = arr[j + 1:]
                j = 0
            res = res + arr
        return res



A = "II"
B = 3
# A = "DD"

# A = "DIDDD"
# B = 6
s = Solution()
print(s.findPerm(A, B))
