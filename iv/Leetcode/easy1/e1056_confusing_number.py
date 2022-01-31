class Solution:
    def confusingNumber(self, n: int) -> bool:
        complement = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

        ns = str(n)
        res = ""
        for i in range(len(ns)):
            if ns[i] not in complement.keys():
                return False
            else:
                res = complement[ns[i]] + res
        print(f"{n} and {int(res)}")
        if int(res) == n:
            return False
        else:
            return True


n = 6
n = 89
n = 11
n = 8080
n = 916
s = Solution()
print(s.confusingNumber(n))


