"""
Given an integer, write a function to determine if it is a power of two.
"""
class Solution():
    def poweroftwo(self, n):
        """
        Using Binary operations
        1 => 0001
        2 => 0010
        4 => 0100
        8 => 1000
        """
        if n < 1:
            return False
        # And operator
        return n & (n - 1) == 0

    def poweroftwo2(self, n):
        """
        Time Complexity: O(n)
        """

        if n < 1:
            return False
        if n == 1:
            return True
        while n > 1:
            if n %2 != 0:
                return False
            n = int(n/2)
        return True

A = 1
A = 16
# A = 218
s = Solution()
print(s.poweroftwo(A))

