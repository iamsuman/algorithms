class Solution:
    def boldWords(self, words: list, S: str) -> str:
        bold = []
        for word in words:
            if len(word) == 0:
                continue
            i = 0
            while i < len(S):
                prefix = S[i:]
                ind = prefix.find(word)
                if ind != -1:
                    l = len(word)
                    for j in range(ind, ind + l):
                        bold.append(i+j)
                    i = i + ind + l
                else:
                    break
        bold = list(set(bold))
        bold.sort()

        # print(bold)
        res = ""
        seq = False
        for i in range(len(S)):
            if i in bold:
                if i == 0:
                    res = "<b>" + S[i]
                else:
                    if seq:
                        res += S[i]
                    else:
                        res = res + "<b>" + S[i]
                seq = True
            else:
                if seq:
                    res = res + "</b>" + S[i]
                else:
                    res += S[i]
                seq = False
        # print(i)
        if seq:
            res += "</b"
        return res


words = ["abc","123"]; S = "abcxyz123"
words = ["aaa","aab","bc"]; S = "aaabbcc"
words = [""]; S = "ccas"
words = [""]; S = ""
# words = ["ab","123"]; S = "abcab"
s = Solution()
print(s.boldWords(words, S))


