class Solution:
    def minOperations(self, nums1: list, nums2: list) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        if sum1 == sum2:
            return 0

        if sum1 > sum2:
            greater_array = nums1
            smaller_array = nums2
        else:
            greater_array = nums2
            smaller_array = nums1

        sum_diff = abs(sum1 - sum2)


        gain1 = [nums - 1 for nums in greater_array]
        gain2 = [6 - nums for nums in smaller_array]
        gain = gain1 + gain2

        gain.sort(reverse=True)
        # print(gain)

        count = 0
        target_diff = sum_diff
        for val in gain:
            if val > 0:
                target_diff -= val
                count += 1
            if target_diff <= 0:
                return count

        return -1


nums1 = [1,2,3,4,5,6]; nums2 = [1,1,2,2,2,2]
nums1 = [1,1,1,1,1,1,1]; nums2 = [6]
nums1 = [2,3];  nums2 = [5]
s = Solution()
print(s.minOperations(nums1, nums2))

