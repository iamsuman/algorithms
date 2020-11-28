class Solution:
    def reverseVowels(self, s: str) -> str:
        slist = list(s)
        # print(slist)
        vowels = "aeiouAEIOU"

        start = 0
        end = len(s) - 1

        while start < end:
            if slist[start] not in vowels:
                start = start + 1
                continue
            if slist[end] not in vowels:
                end = end - 1
                continue
            slist[start], slist[end] = slist[end], slist[start]
            start = start + 1
            end = end -1
        return "".join(slist)


s = "hello"
sol = Solution()
print(sol.reverseVowels(s))

