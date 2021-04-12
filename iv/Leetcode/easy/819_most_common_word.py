from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = paragraph.split(" ")
        d = {}
        for word in words:
            low_word = word.lower()
            for i in range(len(low_word)):
                if not low_word[i].isalpha():
                    low_word = low_word[0:i]
                    break
            if d.get(low_word):
                d[low_word] += 1
            else:
                d[low_word] = 1

        maxwords = 0
        res = ""
        for word in d.keys():
            if word not in banned and d[word] > maxwords:
                maxwords = d[word]
                res = word
        return res


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."; banned = ["hit"]
paragraph = "a."; banned = []
s = Solution()
print(s.mostCommonWord(paragraph, banned))



