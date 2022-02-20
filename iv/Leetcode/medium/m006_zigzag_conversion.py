class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1:
            return s

        numCols = 0
        x = n
        while x > 0:
            x -= numRows
            numCols += 1
            for i in range(numRows - 2):
                if x > 0:
                    numCols += 1
                    x -= 1
        # print(f"numrows: {numRows}, numCols: {numCols}, length of string: {n}")

        arr = []
        for i in range(numRows):
            arr.append([""]*numCols)
        # print(arr)

        down = True
        row = 0
        col = 0
        for i in range(n):
            arr[row][col] = s[i]
            if down:
                row += 1
                if row == numRows - 1:
                    down = False
            else:
                row -= 1
                col += 1
                if row == 0:
                    down = True
        # print(arr)

        res = ""
        for i in range(numRows):
            res += "".join(arr[i])
        return res


s = "PAYPALISHIRING"; numRows = 3
s = "PAYPALISHIRING"; numRows = 4
s = "A"; numRows = 1
# s = "PAYPALISHIRING"; numRows = 1
sol = Solution()
print(sol.convert(s, numRows))


