"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -,
you and your friend take turns to flip two consecutive "++" into "--".
The game ends when a person can no longer make a move and therefore the other person will be the winner.
"""
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i+1] == '+':
                if len(s[i+1:]) > 1:
                    output = s[:i] + "--" + s[i+2:]
                else:
                    output = s[:i] + "--"
                res.append(output)
        return res

s = "++++"
# s = "----"
sol = Solution()
print(sol.generatePossibleNextMoves(s))





