"""
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

"""
class Solution():
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A < 4:
            return 0
        facts = self.factors(A)
        if len(facts) <= 1:
            return 0
        else:
            if len(set(facts)) == 1:
                return 1
            for i in facts:
                if facts.count(i) % 2 != 0:
                    return 0
            return 1

    def factors(self, A):
        # sieve = [True for x in range(A+1)]
        # for i in range(2, A + 1):
        #     if sieve[i]:
        #         for j in range(i * i, A, i):
        #             sieve[j] = False
        fact = []
        i = 2
        while i < int(A / 2 + 2):
            # if sieve[i]:
            while A % i == 0:
                fact.append(i)
                A = int(A / i)
            if i > 2:
                i = i + 2
            else:
                i + 1

        return fact


    # def isPower(self, A):
    #     if A < 3:
    #         return 0
    #     i = 2
    #     while i <= A/2 + 1:
    #         j = i
    #         while j <= A:
    #             if j == A:
    #                 return 1
    #             j = j * i
    #         if i > 2:
    #             i = i + 2
    #         else:
    #             i = i + 1
    #     return 0

s = Solution()
A = 2
A = 81
A = 1024000000
# print(s.isPower(A))
print(s.factors(A))

