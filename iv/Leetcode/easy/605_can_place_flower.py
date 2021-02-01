class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        if n == 0:
            return True
        nums = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if flowerbed[i] == 0:
                # if (i == 0 and flowerbed[i+1] == 0) or (flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                if (i == len(flowerbed) - 1 or flowerbed[i+1] == 0) and (i == 0 or flowerbed[i-1] == 0):
                    nums += 1
                    flowerbed[i] = 1
            if nums >= n:
                return True
        # i = len(flowerbed) - 1
        # if flowerbed[i-1] == 0 and flowerbed[i] == 0:
        #     flowerbed[i] = 1
        #     nums += 1
        # if nums >= n:
        #     return True

        return False

    def canPlaceFlowers2(self, flowerbed: list, n: int) -> bool:
        if n == 0:
            return True
        nums = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
                continue
            if flowerbed[i] == 0:
                # if (i == 0 and flowerbed[i+1] == 0) or (flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                if (i == len(flowerbed) - 1 or flowerbed[i+1] == 0) and (i == 0 or flowerbed[i-1] == 0):
                    nums += 1
                    flowerbed[i] = 1
            if nums >= n:
                return True
            i += 1
        return False


flowerbed = [1,0,0,0,1]; n = 1
flowerbed = [1,0,0,0,1]; n = 2
flowerbed = [1,0,1,0,0]; n = 1
flowerbed = [1]; n = 0
flowerbed = [0,1,0]; n = 1
flowerbed = [0,0,0,0,0,1,0,0]; n = 0
s = Solution()
# print(s.canPlaceFlowers(flowerbed, n))
print(s.canPlaceFlowers2(flowerbed, n))
