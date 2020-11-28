"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
"""
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        reject_list = ["2", "3", "4", "5", "7"]
        strobo = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

        num_list = list(num)
        start = 0
        end = len(num_list) - 1
        while start <= end:
            if num_list[start] in reject_list or num_list[end] in reject_list:
                return False
            if num_list[end] == strobo[num_list[start]]:
                start = start + 1
                end = end - 1
            else:
                return False
        return True


num = "69"
# num = "88"
# num = "1"
s = Solution()
print(s.isStrobogrammatic(num))


