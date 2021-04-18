from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            arr = image[i]
            temp = arr[::-1]
            image[i] = temp

        for i in range(n):
            for j in range(n):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image


image = [[1,1,0]]
s = Solution()
print(s.flipAndInvertImage(image))



