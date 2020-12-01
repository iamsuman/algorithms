class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # TODO Euclid-Euler Theorem
        # num = (2 ** (p - 1)) * (2 ** p - 1) where p is prime
        summ = 1
        if num % 2 != 0:
            return False
        for i in range(2, int(num ** .5) + 1):
            if num % i == 0:
                if i != num / i:
                    summ += (i + num / i)
                else:
                    summ += i
        # print(summ)
        if num == summ:
            return True
        return False



num = 28
# num = 6
# num = 2
# num = 99999998
# num = 6
s = Solution()
print(s.checkPerfectNumber(num))
# for i in range(99999999):
#     if s.checkPerfectNumber(i):
#         print(i)
