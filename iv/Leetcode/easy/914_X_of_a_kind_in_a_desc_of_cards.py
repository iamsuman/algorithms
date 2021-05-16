from typing import List
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        res = {}
        for i in deck:
            res[i] = res.get(i,0) + 1

        # print(res.values())

        gcd = 1
        for i in range(2,min(res.values())+1):
            flag = True
            for val in res.values():
                if val % i != 0:
                    flag = False
                    break
            if flag:
                gcd = i
        # print(gcd)
        if gcd > 1:
            return True
        else:
            return False





deck = [1,2,3,4,4,3,2,1]
deck = [1,1,1,2,2,2,3,3]
deck = [1,1]
deck = [1]
deck = [1,1,2,2,2,2]
deck = [1,1,1,1,2,2,2,2,2,2]

s = Solution()
print(s.hasGroupsSizeX(deck))





