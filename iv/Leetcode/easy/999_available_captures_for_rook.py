from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n = 8
        x = 0
        y = 0
        for i in range(n):
            if "R" in board[i]:
                y = board[i].index("R")
                x = i
                break
        # print(board)
        # print(x,y)

        captures = 0
        for j in range(y+1, n):
            # print(x, j, board[x][j])
            if board[x][j] == "B":
                break
            if board[x][j] == "p":
                captures += 1
                # print("capture")
                break

        for j in range(y-1, -1, -1):
            # print(x, j, board[x][j])
            if board[x][j] == "B":
                break
            if board[x][j] == "p":
                captures += 1
                # print("capture")
                break

        for i in range(x-1, -1, -1):
            # print(i, y, board[i][y])
            if board[i][y] == "B":
                break
            if board[i][y] == "p":
                captures += 1
                # print("capture")
                break
        for i in range(x+1, n):
            # print(i, y, board[i][y])
            if board[i][y] == "B":
                break
            if board[i][y] == "p":
                captures += 1
                # print("capture")
                break
        return captures


board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","B",".",".",".","."],[".","p","B","R","p","B","p","."],[".",".",".","p","p",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
s = Solution()
print(s.numRookCaptures(board))


