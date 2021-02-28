class Solution:
    def countMatches(self, items: list, ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            position = 0
        elif ruleKey == "color":
            position = 1
        elif ruleKey == "name":
            position = 2

        count = 0
        for item in items:
            if item[position] == ruleValue:
                count += 1

        return count


items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]; ruleKey = "color"; ruleValue = "silver"
items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]; ruleKey = "type"; ruleValue = "phone"
s = Solution()
print(s.countMatches(items, ruleKey, ruleValue))

