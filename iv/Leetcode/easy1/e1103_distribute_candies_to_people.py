class Solution:
    def distribute_candies(self, candies, num_people):
        #TODO solve candies = kn*(kn+1)/2
        n = 0
        arr = [0] * num_people
        i = 0
        while candies > 0:
            n += 1
            arr[i] += n if n < candies else candies
            candies -= n
            i += 1
            if i == num_people:
                i = 0

        return arr


candies = 7; num_people = 4
candies = 10; num_people = 3
candies = 10**9; num_people = 1
s = Solution()
print(s.distribute_candies(candies, num_people))

