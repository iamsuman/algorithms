class Solution:
    def findShortestSubArray(self, nums: list) -> int:
        if len(nums) < 2:
            return len(nums)
        degree_dict = {}
        for num in nums:
            if degree_dict.get(num):
                degree_dict[num] += 1
            else:
                degree_dict[num] = 1
        degree = 0
        keys = []
        for key in degree_dict:
            if degree_dict[key] > degree:
                degree = degree_dict[key]
                keys = [key]
            elif degree_dict[key] == degree:
                keys.append(key)

        res = len(nums) + 1
        for key in keys:
            start = -1
            # end = -1
            for i in range(len(nums)):
                if nums[i] == key:
                    if start == -1:
                        start = i
                        end = i
                    else:
                        end = i
            key_len = end - start + 1
            # print(key)
            # print(nums[start:end+1])
            if key_len < res:
                res = key_len
        return res

nums = [1,2,2,3,1]
nums = [1,2,3]
nums = [1,2,2,3,1,4,2]
s = Solution()
print(s.findShortestSubArray(nums))






