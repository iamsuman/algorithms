class Solution:
    def findLHS(self, nums: list) -> int:
        nums.sort()
        start_index = 0
        l_count = 0
        m_count = 0
        LHS = 0

        for i in range(len(nums)):
            if start_index == 0:
                l_count = 1
                min_num = nums[i]
                start_index = 1
                # max_num = None
            else:
                if nums[i] == min_num:
                    l_count += 1
                elif nums[i] - min_num == 1:
                    max_num = nums[i]
                    m_count += 1
                elif m_count != 0 and (nums[i] - max_num == 1):
                    min_num = max_num
                    l_count = m_count
                    m_count = 1
                else:
                    min_num = nums[i]
                    l_count = 1
                    m_count = 0
                    # max_num = min_num + 1
            if l_count and m_count and l_count + m_count > LHS:
                LHS = l_count + m_count

        return LHS


nums = [1,3,2,2,5,2,3,7]
nums = [1,2,3,4]
nums = [1,1,1,1]
nums = [1,3,5,7,9,11,13,15,17]
nums = [1,2,-1,1,2,5,2,5,2]
nums = [3,2,2,3,2,1,3,3,3,-2,0,3,2,1,0,3,1,0,1,3,0,3,3]

s = Solution()
print(s.findLHS(nums))
