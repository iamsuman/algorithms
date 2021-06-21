from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num) - 1
        k_num = self.num_to_array(k)
        kk = len(k_num) - 1

        if kk > n:
            temp = n
            n = kk
            kk = temp
            temp_arr = [i for i in num]
            num = [i for i in k_num]
            k_num = temp_arr

        carry = 0
        while n >= 0 and kk >= 0:
            summ = num[n] + k_num[kk] + carry
            if summ > 9:
                carry = 1
                num[n] = summ % 10
            else:
                carry = 0
                num[n] = summ
            n -= 1
            kk -= 1
        while carry == 1:
            if n >= 0:
                summ = num[n] + carry
                if summ > 9:
                    num[n] = summ % 10
                else:
                    num[n] = summ
                    carry = 0
            else:
                num = [1] + num
                carry = 0
            n -= 1
        return num

    def num_to_array(self, k:int):
        if k == 0:
            return [0]
        k_num = []
        while k > 0:
            k_num.append(k%10)
            k = k // 10
        return k_num[::-1]


num = [2,1,5]; k = 806
num = [9,9,9,9,9,9,9,9,9,9]; k = 1
num = [1,2,0,0]; k = 34
num = [2,7,4]; k = 181
num = [1]; k = 99
num = [6]; k = 809

s = Solution()
print(s.num_to_array(k))
print(s.addToArrayForm(num, k))
