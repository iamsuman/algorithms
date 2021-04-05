from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabets = [chr(i) for i in range(97,123)]
        d = {}
        for a, b in zip(alphabets, morse):
            d[a] = b

        res = set()
        for word in words:
            morse_string = ""
            for s in word:
                morse_string += d[s]
            res.add(morse_string)
        return len(res)

words = ["gin", "zen", "gig", "msg"]

s = Solution()
print(s.uniqueMorseRepresentations(words))
