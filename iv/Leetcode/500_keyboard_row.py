class Solution:
    def findWords(self, words: list) -> list:
        k = ["qwertyuiop","asdfghjkl", "zxcvbnm"]
        res = []

        for word in words:
            if len(word) == 0:
                continue
            if word[0].lower() in k[0]:
                rows = 0
            elif word[0].lower() in k[1]:
                rows = 1
            elif word[0].lower() in k[2]:
                rows = 2

            same_row = True
            for s in word[1:]:
                if s.lower() not in k[rows]:
                    same_row = False
            if same_row:
                res.append(word)
        return res


words = ["Hello", "Alaska", "Dad", "Peace"]
words = [""]
sol = Solution()
print(sol.findWords(words))




