class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = "balloon"
        b1 = {"b": 1, "a": 1, "l": 2, "o": 2, "n":1 }

        text_dict = {}
        for s in text:
            if s in b:
                text_dict[s] = text_dict.get(s,0) + 1

        min_instances = 10 ** 5
        for s in b1:
            if s in text_dict:
                instances = int(text_dict[s] / b1[s])
                if min_instances > instances:
                    min_instances = instances
            else:
                return 0
        return min_instances


text = "nlaebolko"
text = "loonbalxballpoon"
text = "leetcode"
text = "loonbalxballpoo"
sol = Solution()
print(sol.maxNumberOfBalloons(text))




