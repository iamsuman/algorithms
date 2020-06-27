"""
Test
"""
class Solution():
    """
    Class for Solution
    """
    # @param A : tuple of integers
    # @return an integer
    def maxsubarray(self, A):
        """
        # @param A : tuple of integers
        # @return an integer
        """
        if not isinstance(A, (list, tuple)):
            A = tuple([A])
        n = len(A)
        max_sum = -10000
        i = 0

        while i < n:
            mysum = 0
            j = i
            while j < n:
                mysum = mysum + A[j]
                # print("mysum is {}".format(mysum))
                if mysum > max_sum:
                    max_sum = mysum
                j = j + 1
            i = i + 1
        return max_sum


def main():
    # A = [1, 2, 3, 4]
    # A = (-2, 1, -3, 4, -1, 2, 1, -5, 4)
    A = (-500, )
    a = Solution()
    maxsum = a.maxsubarray(A)
    print(maxsum)


if __name__ == '__main__':
    main()
