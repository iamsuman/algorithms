from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, x in enumerate(order):
            d[x] = i

        for i in range(len(words) -1):
            if not self.issorted(words[i], words[i+1], d):
                return False
        return True

    def issorted(self, word1, word2, d):
        i = 0
        while i < len(word1) and i < len(word2):
            if d[word1[i]] > d[word2[i]]:
                return False
            elif d[word1[i]] < d[word2[i]]:
                return True
            i += 1
        if i < len(word1):
            return False
        return True

    def isAlienSorted2(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            if not self.issorted2(words[i], words[i + 1], order):
                return False
        return True

    def issorted2(self, word1, word2, order):
        i = 0
        while i < len(word1) and i < len(word2):
            if order.index(word1[i]) > order.index(word2[i]):
                return False
            elif order.index(word1[i]) < order.index(word2[i]):
                return True
            i += 1
        if i < len(word1):
            return False
        return True


words = ["hello","leetcode"]; order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["word","world","row"]; order = "worldabcefghijkmnpqstuvxyz"
words = ["apple","app"]; order = "abcdefghijklmnopqrstuvwxyz"
s = Solution()
print(s.isAlienSorted(words, order))
print(s.isAlienSorted2(words, order))
