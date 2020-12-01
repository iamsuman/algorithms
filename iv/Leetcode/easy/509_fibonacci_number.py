class Solution:
    def __init__(self):
        self.fn = {0:0, 1:1}

    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if self.fn.get(N):
            return self.fn[N]
        else:
            summ = self.fib(N - 1) + self.fib(N - 2)
            self.fn[N] = summ
            return summ


N = 2
N = 4
s = Solution()
print(s.fib(N))

