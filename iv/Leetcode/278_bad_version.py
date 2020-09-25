def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        # res = check(start, end)

        while start <= end:
            mid = start + int((end - start) / 2)
            if not isBadVersion(mid):
                start = mid + 1
            else:
                end = mid - 1
        return start

