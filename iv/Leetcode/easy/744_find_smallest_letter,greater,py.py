class Solution:
    def nextGreatestLetter(self, letters: list, target: str) -> str:
        res = ""
        min_diff = 27
        tar = ord(target)
        for let in letters:
            if ord(let) > tar:
                diff = ord(let) - tar
            else:
                diff = ord(let) + 27 - tar
            if diff != 0 and diff < min_diff:
                res = let
                min_diff = diff
        return  res

    def nextGreatestLetter2(self, letters, target):
        seen = set(letters)
        for i in xrange(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand


letters = ["c", "f", "j"]
target = "a"

letters = ["c", "f", "j"]
target = "d"

letters = ['a', 'b']
target = 'z'

s = Solution()
print(s.nextGreatestLetter(letters, target))


# res = ""
# min_diff = 27
# diff = 2


