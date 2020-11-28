class Solution():
    def intersection(self, nums1, nums2):
        # Time Complexity: O(n + m)
        # Space Complexity: O(n + m)
        set1 = set(nums1)
        set2 = set(nums2)
        return [x for x in set1 if x in set2]

    def intersection2(self, nums1, nums2):
        # Time Complexity n * m
        intersect = []
        for i in range(len(nums1)):
            if nums1[i] in intersect:
                continue
            if nums1[i] in nums2:
                intersect.append(nums1[i])
        return intersect


nums1 = [1,2,2,1]
nums2 = [2,2]

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
s = Solution()
print(s.intersection(nums1, nums2))


