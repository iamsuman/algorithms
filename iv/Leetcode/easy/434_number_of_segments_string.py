class Solution:
    def countSegments(self, s: str) -> int:
        counter = 0
        segment = False
        for i in range(len(s)):
            if s[i] == " ":
                if segment:
                    counter += 1
                    segment = False
            else:
                segment = True
        if segment:
            counter += 1
        return counter

    def countSegments2(self, s: str) -> int:
        return len(s.split())


s = "Hello, my name is John"
s = "Hello"
# s = ""
# s = "                       "
sol = Solution()
print(sol.countSegments(s))
