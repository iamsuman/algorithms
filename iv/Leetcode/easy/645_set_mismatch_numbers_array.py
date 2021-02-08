class Solution:
    def findErrorNums(self, nums: list) -> list:
        # TIme Complexity: O(n)
        # Space Complexity: O(n)
        # TODO Space O(1): use XOR
        d = {}
        rep_number = 0
        for i in nums:
            if d.get(i):
                rep_number = i
                d[i] += 1
            else:
                d[i] = 1
        for i in range(1, len(nums) + 1):
            if d.get(i):
                pass
            else:
                missing_number = i
                break
        return [rep_number, missing_number]


nums = [1,2,2,4]
nums = [1,1]
s = Solution()
print(s.findErrorNums(nums))


