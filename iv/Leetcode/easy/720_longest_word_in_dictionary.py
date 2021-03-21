class Solution:
    def longestWord(self, words: list) -> str:
        res = []
        maxlength = 0
        words.sort(key=lambda word: len(word), reverse=True)
        # print(words)
        for word in words:
            l = len(word)
            found = True
            for i in range(l):
                if word[:i+1] not in words:
                    found = False
                    break
            if not found:
                continue
            else:
                if maxlength < len(word):
                    maxlength = len(word)
                    res = [word]
                elif maxlength == len(word):
                    res.append(word)
        res.sort()
        if len(res) > 0:
            return res[0]
        else:
            return []


words = ["w","wo","wor","worl", "world"]
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# words =["a"]
s = Solution()
print(s.longestWord(words))
