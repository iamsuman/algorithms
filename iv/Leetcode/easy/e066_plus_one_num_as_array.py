from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        start = 1
        for i in range(len(digits)-1, -1, -1):
            summ = digits[i] + start + carry
            if summ > 9:
                digits[i] = summ - 10
                carry = 1
            else:
                digits[i] = summ
                return digits
                carry = 0
            start = 0
        if carry == 1:
            digits = [1] + digits

        return digits


digits = [1,2,3]
digits = [4,3,2,1]
digits = [0]
digits = []
digits = [9,9,9]
s = Solution()
print(s.plusOne(digits))



