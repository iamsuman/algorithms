class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(" ")
        for i in range(len(words)):
            word = words[i]
            if word[0].lower() in ("a","e","i","o","u"):
                newword = word + "ma" + "a"*(i+1)
            else:
                if len(word) > 1:
                    newword = word[1:] + word[0] + "ma" + "a"*(i+1)
                else:
                    newword = word + "ma" + "a" * (i + 1)
            words[i] = newword
        return " ".join(words)


S = "I speak Goat Latin"
S = "HZ sg L"
s = Solution()
print(s.toGoatLatin(S))
