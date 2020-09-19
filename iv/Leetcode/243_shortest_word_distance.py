"""
Given a list of words and two words word1 and word2,
return the shortest distance between these two words in the list
"""
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dist = len(words) + 1
        i1 = -1
        i2 = -1
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
            elif words[i] == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                if dist > abs(i1 - i2):
                    dist = abs(i1 - i2)
        return dist


words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"

word1 = "makes"
word2 = "coding"

s = Solution()
print(s.shortestDistance(words, word1, word2))




