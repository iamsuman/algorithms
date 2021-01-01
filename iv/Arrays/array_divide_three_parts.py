# arr = [ 1, 2, 3, 0, 3]

class Solution():
    def divide_array(self, A, B):
        i = 0
        summ = sum(B)
        if int(summ % 3) != 0:
            return 0
        first_sum = int(summ / 3)
        res = []
        while i < A - 2:
            j = i + 1
            # print(i, j)
            lsum = sum(B[:i + 1])
            if lsum != first_sum:
                i += 1
                continue
            msum = sum(B[i + 1:j + 1])
            rsum = sum(B[j + 1:])
            while j < A - 1:
                # print(i, j, lsum, msum, rsum)
                if lsum == msum == rsum:
                    res.append([B[:i+1], B[i+1: j + 1], B[j+1:]])
                j += 1
                msum = msum + B[j]
                rsum = rsum - B[j]
            i += 1
        return len(res)

    def solve(self, A, B):
        # A = len(B)

        counter = 0
        for i in range(A - 1):
            # print()
            for j in range(i + 1, A - 1):
                lsum = sum(B[:i + 1])
                msum = sum(B[i + 1:j + 1])
                rsum = sum(B[j + 1:])
                # print(f'0:{i + 1} {i + 1}:{j + 1} {j + 1}:{A}')
                if lsum == msum == rsum:
                    # print(B[0:i + 1], B[i + 1:j + 1], B[j + 1:A])
                    counter += 1

        return counter

    def solve2(self, A, B):
        summ = sum(B)
        if summ % 3 == 0:
            target = summ // 3
        else:
            return 0

        ans = 0
        f = 0
        s = 0
        # Find the mid array
        for i in range(A - 1):
            s += B[i]
            if s == 2 * target:
                ans += f
            if s == target:
                f += 1
        return ans



# B = [ 1, 2, 3, 0, 3]; A = 5
# B = [0, 1, -1 , 0]; A = 4
A = 4
B = [0, 2, -1, 2]
# A = 5
# B = [1, 2, 3, 0, 3]
#
# A = 5
# B = [3, 3, -3, 3, 3]
# A = 8
# B = [3, 3, -3, 3, 3, -1, -2, 3]
# A = 4
# B = [0, 1, -1, 0]
# A = 6
# B = [0, 1, 0, -1, 0, 0]
# A = 9
# B = [1, 0, -1, 1, 0, 0, 1, 0, 1]
# A = 8
# B = [0, -3, 1, 2, -2, 0, 0, 2]
# A = 6
# B = [0, 0, 0, 0, 0, 0]
A = 5; B = [ 1, 2, 3, 0, 3 ]

s = Solution()
print(s.divide_array(A, B))
print(s.solve(A, B))
# print(s.solve2(A, B))


