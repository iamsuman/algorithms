class Wave():
    def wave_array(self, A):
        A.sort()
        for i in range(0, len(A) - 1, 2):
            temp = A[i]
            A[i] = A[i + 1]
            A[i + 1] = temp
        return A


def main():
    A = [3, 2, 1, 3]
    # A = [-1, 0, -1]
    # A = [6, 7, 5]
    # A = [-6, -1, 4]

    a = Wave()
    print(a.wave_array(A))


if __name__ == '__main__':
    main()

