class Solution:
    def distributeCandies(self, candyType: list) -> int:
        num_candies = int(len(candyType) / 2)
        n_distinct = len(set(candyType))
        return min(num_candies, n_distinct)


candyType = [1,1,2,2,3,3]
candyType = [6,6,6,6]
s = Solution()
print(s.distributeCandies(candyType))

