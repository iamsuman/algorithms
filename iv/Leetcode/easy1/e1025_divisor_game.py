class Solution:
    def divisorGame(self, n: int) -> bool:
        div = [False] * (n + 1)
        div[1] = False
        if n == 1:
            return div[1]
        div[2] = True
        for i in range(3, n+1):
            x = [x for x in range(1,i) if i%x == 0]
            # print(f"factors of {i}: {x}")
            for y in x:
                if i - y > 0 and not div[i-y]:
                    div[i] = True
                    break
            # print(f"{i} factores are {x}")
        print(div)
        return div[n]

    def divisorGame2(self, n: int) -> bool:
        return n % 2 == 0


n = 2
n = 3
n = 4
n = 100
# n = 1
s = Solution()
print(s.divisorGame(n))
print(s.divisorGame2(n))


