class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        res = []
        for i in nums1:
            start = False
            found = False
            for j in nums2:
                if j == i:
                    start = True
                    continue
                if start and j > i:
                    res.append(j)
                    found = True
                    break
            if not found:
                res.append(-1)
        return res


nums1 = [4,1,2]; nums2 = [1,3,4,2]
nums1 = [2,4]; nums2 = [1,2,3,4]
nums1 = [1]; nums2 = [1]
s = Solution()
print(s.nextGreaterElement(nums1, nums2))

# res =
# i = 4, 1
# j = 1, 3, 4, 2
# start = False, True
# found = false





