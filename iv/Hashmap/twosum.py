class Tsum():
    """
    Given an array of integers, find two numbers such that they add up to a specific target number.
    Input: [2, 7, 11, 15], target=9
    Output: index1 = 1, index2 = 2
    """
    def twosum2(self, A, B):
        myhash = {}
        res = []
        for i in range(len(A)):
            # if A[i] > target:
            #     continue
            if myhash.get(A[i]):
                # print(myhash)
                # res.append((i, myhash[A[i]]))
                return [myhash[A[i]][0] + 1, i + 1]
            else:
                mydiff = B - A[i]
                if myhash.get(mydiff):
                    myhash[mydiff].append(i)
                else:
                    myhash[mydiff] = [i]
        return res


t = Tsum()
A = [2, 7, 11, 15]
target=9

A = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
target = -3

print(t.twosum2(A, target))


