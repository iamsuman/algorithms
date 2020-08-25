"""
Given a set of distinct integers, S, return all possible subsets.
"""


class Solution():
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        # TODO
        if A == None or len(A) < 1:
            temp = []
            temp.append([])
            return temp;

            # Sort the list and pass the
            # attributes to recursive function.
        A = sorted(A)
        result = []
        subset = []
        self.findSubsets(A, result, subset, 0)

        # result.sort()
        return result

        # @param A : list of integers
        # @param result : list of list of integers conatining subsets
        # @param subset : list of integers for subsets
        # @param index : integer for start index
        # @return None

    def findSubsets(self, A, result, subset, index):
        # Add elements of subset list to result
        # list in every recursive step.
        temp = []
        for i in range(len(subset)):
            temp.append(subset[i])
        result.append(temp)

        # Iterate over all the elements of A.
        for i in range(index, len(A)):
            subset.append(A[i])
            self.findSubsets(A, result, subset, i + 1)
            subset.pop()


A = [1, 2, 3, 4, 5]
# A = [15, 20, 12, 19, 4]
s = Solution()
print(s.subsets(A))
