class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list) -> str:
        lp = {}
        licensePlate = licensePlate.lower()
        for i in range(len(licensePlate)):
            if licensePlate[i].isalpha():
                if lp.get(licensePlate[i]):
                    lp[licensePlate[i]] += 1
                else:
                    lp[licensePlate[i]] = 1
        # print(lp)

        res = ""
        min_len = 16
        for word in words:
            found = True
            for s in lp.keys():
                # print(word.count(s))
                if word.count(s) < lp[s]:
                    found = False
                    break
            if found and len(word) < min_len:
                res = word
                min_len = len(word)
        return res


licensePlate = "1s3 PSt"; words = ["step","steps","stripe","stepple"]
licensePlate = "1s3 456"; words = ["looks","pest","stew","show"]
s = Solution()
print(s.shortestCompletingWord(licensePlate, words))

