class Solution:
    def thirdMax(self, nums: list) -> int:
        myhash = []
        found = True
        while len(myhash) < 3 and found:
            # TODO add code for min integer
            mymax = -2 ** 31 - 1
            print(mymax)
            found = False
            for n in nums:
                if n not in myhash and n > mymax:
                    found = True
                    mymax = n
            if found:
                myhash.append(mymax)
        if len(myhash) == 3:
            return myhash[2]
        else:
            return myhash[0]

nums = [3, 2, 1]
nums = [2, 2, 3, 1]
nums = [1,2]
nums = [1, 2, -2147483648]
s = Solution()
print(s.thirdMax(nums))

