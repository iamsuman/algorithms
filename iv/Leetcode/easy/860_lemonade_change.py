from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {}
        for amt in bills:
            # if amt == 5:
            #     pass
            if amt == 10:
                if change.get(5):
                    change[5] -= 1
                else:
                    return False
            if amt == 20:
                if change.get(10) and change.get(5):
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
            if change.get(amt):
                change[amt] += 1
            else:
                change[amt] = 1
        return True


bills = [5,5,5,10,20]
bills = [5,5,10]
bills = [10,10]
bills = [5,5,10,10,20]
s = Solution()
print(s.lemonadeChange(bills))
