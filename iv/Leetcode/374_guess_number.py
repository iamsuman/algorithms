n = 10
pick = 6
# n = 100
# pick = 78
# n = 2
# pick = 2


def guess(num: int) -> int:
    if num < pick:
        return -1
    elif num == pick:
        return 0
    else:
        return 1


class Solution:
    def guessNumber(self, n: int):
        # Time Complexity O(log(n))
        # Space Complexity : O(1)

        start = 1
        end = n
        # iter = 0

        while True:
            # iter += 1
            myguess = int((start + end) / 2)
            # print(iter, myguess)
            res = guess(myguess)
            if res == -1:
                start = myguess + 1
            elif res == 1:
                end = myguess - 1
            else:
                return myguess

s = Solution()
print(s.guessNumber(n))




