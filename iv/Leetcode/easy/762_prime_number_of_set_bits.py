class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        prime_numbers = [2,3,5,7,11,13,17,19]
        count = 0
        for i in range(L, R+1):
            if self.binary(i).count("1") in prime_numbers:
                count += 1
        return count

    def binary(self, num):
        if num == 0:
            return "0"
        res = ""
        while num > 0:
            res = str(num % 2) + res
            num = int(num / 2)
        return res


L = 6; R = 10
L = 10; R = 15
s = Solution()
print(s.countPrimeSetBits(L, R))
# print(s.binary(0))
