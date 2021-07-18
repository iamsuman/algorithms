class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_len = 0
        found = False
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if last_len != 0:
                    break
            else:
                last_len += 1
        return last_len

    def lengthOfLastWord2(self, s: str) -> int:
        res = s.strip().split(" ")
        # print(res)
        if len(res) == 0:
            return 0
        last_word = res[-1]
        return len(last_word)


s = "Hello World"
s = " "
# s = " a "
obj = Solution()
print(obj.lengthOfLastWord(s))
print(obj.lengthOfLastWord2(s))
