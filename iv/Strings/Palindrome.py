class Palindrome():
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        n = len(A)
        if len(A) < 2:
            return 1
        i = 0
        j = n -1
        while i < j:
            if (A[i]).isalnum() and (A[j]).isalnum():
                print((A[i]).lower())
                print(A[j].lower())
                if A[i].lower() == A[j].lower():
                    i = i + 1
                    j = j - 1
                    continue
                else:
                    return 0
            elif not (A[i]).isalnum():
                i = i + 1
            elif not (A[j]).isalnum():
                j = j - 1
        return 1


A = "A man, a plan, a canal: Panama"
# A = "race a car"
# # A = ""
# A = "a"
A = "abba"
A = "aba"
A = "Malayalam"

a = Palindrome()
print(a.isPalindrome(A))

