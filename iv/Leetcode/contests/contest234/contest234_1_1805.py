class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        res = set()
        num = ""
        for i in range(len(word)):
            if word[i].isnumeric():
                num += word[i]
            elif len(num) != 0:
                # print(num)
                res.add(int(num))
                num = ""
        if len(num) != 0:
            res.add(int(num))
        return len(res)


word = "a1b01c001"
word = "leet1234code234"
word = "a123bc34d8ef34"
word = ""

s = Solution()
print(s.numDifferentIntegers(word))




