class Solution():
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        if len(nums1) < len(nums2):
            res = self.find_intersect(nums1, nums2)
        else:
            res = self.find_intersect(nums2, nums1)
        return res

    def find_intersect(self, n1, n2):
        intersect = []
        i = 0
        j = 0
        while i < len(n1) and j < len(n2):
            if n1[i] == n2[j]:
                intersect.append(n1[i])
                i += 1
                j += 1
            elif n1[i] < n2[j]:
                i += 1
            else:
                j += 1
        return intersect


nums1 = [1,2,2,1]
nums2 = [2,2]

nums1 = [1,2,2,1]
nums2 = [2]

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
s = Solution()
print(s.intersection(nums1, nums2))


