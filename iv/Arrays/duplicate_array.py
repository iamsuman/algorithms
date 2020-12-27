import sys


class Duplicate():
    def duplicate_array(self, A):
        # A = [1, 2, 3, 3, 4, 4, 5]
        n = len(A)
        start = 0
        while start < n - 2:
            if A[start] < A[start + 1]:
                start = start + 1
                continue
            else:
                for end in range(start + 1, n):
                    if A[start] >= A[end]:
                        continue
                    else:
                        A[start + 1] = A[end]
                        break
            start = start + 1
        return A

    def remove_duplicate2(self, A):
        # A = [-3, -3, 3, 3, 3, 5, 9, 11, 11, 13]
        if len(A) < 2:
            return len(A)
        for i in range(len(A) - 1):
            # print(A)
            if A[i] >= A[i + 1]:
                lo = i + 1
                swapped = False
                while lo < len(A):
                    if A[lo] > A[i]:
                        A[lo], A[i+1] = A[i+1], A[lo]
                        swapped = True
                        break
                    else:
                        lo = lo + 1

                if not swapped:
                    break
        # print(A)
        for i in range(len(A) - 1):
            # print(i)
            if A[i] >= A[i + 1]:
                return i + 1
        return i + 2






def main():
    A = [1, 2, 3, 3, 4, 4, 5]
    A = [-3, -3, 3, 3, 3, 5, 9, 11, 11, 13]
    A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]
    A = [5000, 5000, 5000]
    A = [ 0, 1, 3 ]
    a = Duplicate()
    # print(a.duplicate_array(A))
    print(a.remove_duplicate2(A))


if __name__ == "__main__":
    main()



