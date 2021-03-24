class Solution:
    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        # DFS
        r = len(image)
        if r > 0:
            c = len(image[0])
        else:
            c = 0
        orig_color = image[sr][sc]
        myheap = [(sr, sc)]
        visited = []
        while len(myheap) > 0:
            i, j = myheap.pop(0)
            image[i][j] = newColor
            if 0 <= i - 1 < r and image[i - 1][j] == orig_color and (i - 1, j) not in visited:
                myheap.append((i - 1, j))
                visited.append((i - 1, j))
                # image[i - 1][j] = newColor
            if 0 <= i + 1 < r and image[i + 1][j] == orig_color and (i + 1, j) not in visited:
                myheap.append((i + 1, j))
                visited.append((i + 1, j))
                # image[i + 1][j] = newColor
            if 0 <= j - 1 < c and image[i][j - 1] == orig_color and (i, j - 1) not in visited:
                myheap.append((i, j - 1))
                visited.append((i, j - 1))
                # image[i][j - 1] = newColor
            if 0 <= j + 1 < c and image[i][j + 1] == orig_color and (i, j + 1) not in visited:
                myheap.append((i, j + 1))
                visited.append((i, j + 1))
                # image[i][j + 1] = newColor
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1;
sc = 1;
newColor = 2

# image = [[0, 0, 0], [0, 1, 0]]
# sr = 1; sc = 1;
# newColor = 2
s = Solution()
print(s.floodFill(image, sr, sc, newColor))
