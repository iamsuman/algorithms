from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        text_list = text.split()
        for i in range(2, len(text_list)):
            if text_list[i-2] == first and text_list[i-1] == second:
                res.append(text_list[i])
        return res


text = "alice is a good girl she is a good student"; first = "a"; second = "good"
text = "we will we will rock you"; first = "we"; second = "will"
s = Solution()
print(s.findOcurrences(text, first, second))
