class Solution:
    def judgeCircle(self, moves: str) -> bool:
        myheap = {}
        for i in moves:
            if myheap.get(i):
                myheap[i] += 1
            else:
                myheap[i] = 1

        if myheap.get("U", 0) - myheap.get("D", 0) == 0 and myheap.get("R", 0) - myheap.get("L", 0) == 0:
            return True
        else:
            return False

    def judgeCircle2(self, moves: str) -> bool:
        x = 0
        y = 0
        for i in moves:
            if i == 'U':
                y += 1
            elif i == 'D':
                y -= 1
            elif i == 'R':
                x += 1
            elif i == 'L':
                x -= 1

        return x == 0 and y == 0




moves = "UD"
# moves = "LL"
# moves = "LDRRLRUULR"
s = Solution()
print(s.judgeCircle(moves))
print(s.judgeCircle2(moves))
