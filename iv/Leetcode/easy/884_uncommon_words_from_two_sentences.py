from typing import List
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split()
        B = B.split()
        d = {}
        for ss in A:
            if d.get(ss):
                d[ss] += 1
            else:
                d[ss] = 1
        for ss in B:
            if d.get(ss):
                d[ss] += 1
            else:
                d[ss] = 1
        res = []
        for key in d.keys():
            if d[key] == 1:
                res.append(key)

        return res


A = "this apple is sweet"; B = "this apple is sour"
# A = "apple apple"; B = "banana"
s = Solution()
print(s.uncommonFromSentences(A, B))



