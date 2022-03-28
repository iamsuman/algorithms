from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            while res and self.get_gcd(res[-1], num) > 1:
                num = self.get_lcm(res[-1], num)
                res.pop()
            res.append(num)
        return res

    def replaceNonCoprimes2(self, nums: List[int]) -> List[int]:
        found = True
        while found:
            found = False
            i = 0
            while i < len(nums) - 1:
                # print(f"{nums[i]}, {nums[i+1]}")
                gcd = self.get_gcd(nums[i], nums[i + 1])
                if gcd == 1:
                    i += 1
                else:
                    lcm = int(nums[i] * nums[i + 1] / gcd)
                    nums = nums[:i] + [lcm] + nums[i+2:]
                    found = True
        return nums

    def get_gcd(self, n1, n2):
        if n1 == n2:
            return n1
        if n1 > n2:
            n1, n2 = n2, n1
        if n2 % n1 == 0:
            return n1
        res = 1
        while n1 % 2 == 0 and n2 % 2 == 0:
            res = res * 2
            n1 = n1 // 2
            n2 = n2 // 2
        for i in range(3, n1 // 2 + 2, 2):
            while n1 % i == 0 and n2 %i == 0:
                res = res * i
                n1 = n1 // i
                n2 = n2 //i
        return res

    def get_gcd2(self, n1, n2):
        if n1 == n2:
            return n1
        if n1 > n2:
            n1, n2 = n2, n1
        res = 1
        while n2 - n1 > 1:
            if n2 % n1 == 0:
                res = n1
                break
            n1, n2 = n1, n2 - n1
            if n1 > n2:
                n1, n2 = n2, n1
        # print(res)
        return res

    def get_lcm(self, n1, n2):
        gcd = self.get_gcd(n1, n2)
        return int(n1 * n2 / gcd)


s = Solution()
# print(s.get_gcd(899, 20677))
# print(s.get_gcd(899, 23))
print(s.get_lcm(3,12))
nums = [6,4,3,2,7,6,2]
# nums = [2,2,1,1,3,3,3]
# nums = [287,41,49,287,899,23,23,20677,5,825]
print(s.replaceNonCoprimes(nums))
print(s.replaceNonCoprimes2(nums))

