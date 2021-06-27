from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = [[] for i in range(n+1)]
        for [i,j] in trust:
            d[i].append(j)
        # print(d)

        judge_list = []
        for i in range(1, n+1):
            if len(d[i]) == 0:
                judge_list.append(i)

        if len(judge_list) == 0:
            return -1

        res = []
        for i in judge_list:
            is_judge = True
            for j in range(1,n+1):
                if j == i:
                    continue
                else:
                    if i not in d[j]:
                        is_judge = False
                        break
            if is_judge:
                res.append(i)

        if len(res) == 1:
            return res[0]
        else:
            return -1


n = 2; trust = [[1,2]]
n = 3; trust = [[1,3],[2,3]]
n = 3; trust = [[1,3],[2,3],[3,1]]
n = 3; trust = [[1, 2], [2, 3]]
n = 4; trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
s = Solution()
print(s.findJudge(n, trust))

