class Triplet():
    def triplet_sum(self, A):
        ret = 0
        count = 0
        A = list(map(lambda s: float(s), A))
        A.sort()
        n = len(A)
        B = []
        for i in range(len(A)):
            if A[i] < 2.0:
                B.append(A[i])
        print(B)
        n = len(B)
        for i in range(0, n):
            for j in range(i+1, n):
                if ret == 1:
                    break
                # if i == j:
                #     continue
                for k in range(j+1, n):
                    if ret == 1:
                        break
                    # if i == k or j == k:
                    #     continue
                    else:
                        count = count + 1
                        mysum = B[i] + B[j] + B[k]
                        # print(i, j, k)
                        # print(mysum)
                        if 1 < mysum < 2:
                            ret = 1
                            break
        print(count)
        return ret


def main():
    A = [0.6, 0.7, 0.8, 1.2, 0.4]
    A = ["2.673662", "2.419159", "0.573816", "2.454376", "0.403605", "2.503658", "0.806191"]
    A = ["0.366507", "0.234601", "2.126313", "1.372403", "2.022170", "0.308558", "2.120754", "1.561462"]
    # A = [ "0.503094", "0.648924", "0.999298" ]
    a = Triplet()
    print(a.triplet_sum(A))


if __name__ == '__main__':
    main()

