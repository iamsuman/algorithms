class Noble():
    """
    Time Limit Exceeded. Your submission didn't complete in the allocated time limit.
    """
    def noble_integer(self, A):
        """

        """
        # A = [3, 2, 1, 3]
        noble = -1
        for i in set(A):
            # print(i)
            n = 0
            for j in A:
                if i < j:
                    n = n + 1
            if i == n:
                noble = 1
                break
        return noble

    def noble_integer2(self, A):
        A.sort()
        noble = -1
        for i in set(A):
            B = A[::-1]
            n = 0
            for j in B:
                if j > i:
                    print(i,j)
                    n = n + 1
                else:
                    break
            if i == n:
                noble = 1
                break
        return noble

    def noble_integer3(self, A):
        A.sort()
        noble = -1
        for i in set(A):
            n = len([j for j in A if j > i])
            if i == n:
                noble = 1
        return noble


def main():
    a = Noble()
    A = [3, 2, 1, 3]
    print(a.noble_integer2(A))


if __name__ == '__main__':
    main()


