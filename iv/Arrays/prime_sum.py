class Prime():
    def primesum(self, A):
        if A == 4:
            return [2, 2]
        sieve = [True for i in range(A + 1)]
        for i in range(2, A + 1):
            if sieve[i]:
                for j in range(i * i, A, i):
                    sieve[j] = False

        for i in range(3, A, 2):
            if sieve[i] and sieve[A - i]:
                return [i, A - i]

    def prime_sum(self, A):
        # mylist = self.prime_list_1(A)
        mylist = self.prime_list(A)
        for i in (mylist):
            if A - i in mylist:
                return i, A - i
        # Sieve
        # for i in

    def prime_list(self, n):
        A = [2]
        i = 3
        while i < n:
            if self.isprime(i):
                A.append(i)
            i = i + 2
        return A

    def prime_list_1(self,n):
        # Sieve of Eratosthenes
        A = [1] * n
        A[0] = 0
        A[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            j = 2
            while i * j < n:
                A[i * j] = 0
                j = j + 1
        myprime_list = []
        for i in range(n):
            if A[i] == 1:
                myprime_list.append(i)
        return myprime_list

    def isprime(self, p):
        if p%2 == 0:
            return False
        else:
            i = 3
            while i < p ** 0.5 + 1:
                if p % i == 0:
                    return False
                i = i + 2
        return True

a = Prime()
# print(a.isprime(10))
# print(a.prime_list_1(100))
# print(a.primesum(200))
print(a.primesum(4))
print(a.primesum(16777214))
# print(a.primesum(16777214))
