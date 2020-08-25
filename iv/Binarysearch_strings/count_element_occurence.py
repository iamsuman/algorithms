"""
Given a sorted array of integers, find the number of occurrences of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return 0
"""
class Solution():
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        start = 0
        end = len(A) - 1
        index = -1
        if len(A) == 1 and A[0] == B:
            return 1
        while start < end:
            mid = int((start + end) / 2)
            if A[mid] == B:
                index = mid
                break
            elif A[mid] > B:
                end = mid -1
            else:
                start = mid + 1
        if index == -1:
            return 0
        else:
            # right
            count = 1
            r_index, l_index = index, index
            while r_index + 1 < len(A):
                if A[r_index+1] == B:
                    count = count + 1
                else:
                    break
                r_index = r_index + 1
            while l_index - 1 >= 0:
                if A[l_index-1] == B:
                    count = count + 1
                else:
                    break
                l_index = l_index -1
        return count


A = [5, 7, 7, 8, 8, 10]
B = 8

A = [1]
B =1

# A = [ 4, 7, 7, 7, 8, 10, 10 ]
# B = 3
s = Solution()
print(s.findCount(A, B))
