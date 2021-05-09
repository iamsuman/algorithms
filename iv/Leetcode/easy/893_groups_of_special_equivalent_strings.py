from typing import List


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        d = {}
        for word in A:
            odd = []
            even = []
            for i in range(len(word)):
                if i % 2 == 0:
                    even.append(word[i])
                else:
                    odd.append(word[i])

            odd.sort()
            even.sort()
            k = tuple([tuple(odd), tuple(even)])
            d[k] = d.get(k,0) + 1
        # print(d)
        return len(d)


A = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
A = ["abc","acb","bac","bca","cab","cba"]
s = Solution()
print(s.numSpecialEquivGroups(A))
