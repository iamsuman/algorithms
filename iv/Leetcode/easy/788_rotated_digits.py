class Solution:
    def rotatedDigits(self, N: int) -> int:
        # TODO check DP
        count = 0
        for i in range(1,N+1):
            if self.rotate(i):
                count += 1
                print(i)
        return count

    def rotate(self, num):
        rev = {1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6, 0: 0}
        rot_num = ""
        for s in str(num):
            if rev.get(int(s)) is None:
                return False
            else:
                rot_num += str(rev.get(int(s)))
        # print(rot_num)

        if num == int(rot_num):
            return False
        else:
            return True


N = 10
N = 100
s = Solution()
print(s.rotatedDigits(N))




