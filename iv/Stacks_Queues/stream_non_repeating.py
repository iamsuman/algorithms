"""
Given a string A denoting a stream of lowercase alphabets. You have to make new string B.

B is formed such that we have to find first non-repeating character each time a character
is inserted to the stream and append it at the end to B. If no non-repeating character
is found then append '#' at the end of B.
"""
class Solution():
    # @param A : string
    # @return a strings
    def solve(self, A):
        # TODO
        #  solve again
        res = ""
        MAX_CHAR = 256
        # inDLL[x] contains pointer to a DLL node if x is present
        # in DLL. If x is not present, then inDLL[x] is NULL
        inDLL = [] * MAX_CHAR

        # repeated[x] is true if x is repeated two or more times.
        # If x is not seen so far or x is seen only once. then
        # repeated[x] is false
        repeated = [False] * MAX_CHAR

        # Let us consider following stream and see the process
        for i in range(len(A)):
            x = A[i]
            # print("Reading " + x + " from stream")

            # We process this character only if it has not occurred
            # or occurred only once. repeated[x] is true if x is
            # repeated twice or more.s
            if not repeated[ord(x)]:

                # If the character is not in DLL, then add this
                # at the end of DLL
                if not x in inDLL:
                    inDLL.append(x)
                else:
                    inDLL.remove(x)
                    repeated[ord(x)] = True

            if len(inDLL) != 0:
                # print("First non-repeating character so far is ")
                # print(str(inDLL[0]))
                res = res + str(inDLL[0])
            else:
                res = res + "#"
        return res


    def solve2(self, A):
        st = {}
        res = ""

        for i in range(len(A)):
            if st.get(A[i]):
                st[A[i]] += 1
            else:
                st[A[i]] = 1

            found = False
            for j in A[:i+1]:
                if st[j] == 1:
                    res = res + j
                    found = True
                    break
            if not found:
                res = res + "#"

        return res


A = "abadbc"
A = "abcabc"
s = Solution()
print(s.solve(A))

