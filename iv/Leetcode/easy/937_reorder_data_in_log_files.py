from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        llogs = []
        dlogs = []
        for log in logs:
            mylist = log.split(" ")
            if mylist[1].isalpha():
                # llogs.append(mylist)
                ml = [str(mylist[0])] + [" ".join(mylist[1:])]
                llogs.append(ml)
            else:
                dlogs.append(mylist)
        llogs.sort(key=lambda ll: (ll[1], ll[0]))
        ans = []
        for ll in llogs:
            ans.append(" ".join(ll))
        for dl in dlogs:
            ans.append(" ".join(dl))

        return ans


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
s = Solution()
print(s.reorderLogFiles(logs))
