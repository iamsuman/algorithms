class Solution:
    def calPoints(self, ops: list) -> int:
        res = []
        for item in ops:
            if item == "+":
                res.append(res[-1] + res[-2])
            elif item == "D":
                res.append(res[-1] * 2)
            elif item == "C":
                res.pop(-1)
            else:
                res.append(int(item))

        # print(res)
        return sum(res)


ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]
ops = ["1"]
s = Solution()
print(s.calPoints(ops))
