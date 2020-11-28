"""
You are playing the following Nim Game with your friend:
There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.
The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
"""
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4 == 0:
            return True
        else:
            return False
