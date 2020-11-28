"""
Write an algorithm to determine if a number n is "happy"
"""
class Solution(object):
    def isHappy(self, n):
        slow = n
        fast = self.sq_sum(n)

        while fast != 1 and slow != fast:
            slow = self.sq_sum(slow)
            fast = self.sq_sum(self.sq_sum(fast))
        return fast == 1


    def isHappy2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        n_hash = []
        while n >= 1:
            sqsum = self.sq_sum(n)
            if sqsum == 1:
                return True
            if sqsum in n_hash:
                return False
            else:
                n_hash.append(sqsum)
            n = sqsum

    def sq_sum(self, n):
        summ = 0
        while n > 0:
            summ = summ + (n%10) ** 2
            # print(n, summ)
            n = int(n/10)
        return summ
        # n_list = list(str(n))
        # nlist = map(int, n_list)
        # nlist = map(lambda x: x ** 2, nlist)
        # return sum(nlist)


A = 19
# A = 20
s = Solution()
print(s.isHappy(A))


