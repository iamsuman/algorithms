class Points():
    """
    Path Traversed
    """
    def coverpoints(self, A, B):
        """
        Function to find steps traversed
        A is list of x coordinates
        B is list of y coordinates
        """
        # A = [0, 1, 1]
        # B = [0, 1, 2]
        n = len(A)
        total_steps = 0
        for i in range(n - 1):
            x_steps = abs(A[i + 1] - A[i])
            y_steps = abs(B[i + 1] - B[i])
            steps = min(x_steps, y_steps) + abs(x_steps - y_steps)
            # print(steps)
            total_steps = total_steps + steps
            # print(total_steps)
        return total_steps


def main():
    a = Points()
    # A = [0, 1, 1]
    # B = [0, 1, 2]

    A = [4, 8, -7, -5, -13, 9, -7, 8]
    B = [4, -15, -10, -3, -13, 12, 8, -8]

    dist = a.coverpoints(A, B)
    print(dist)


if __name__ == '__main__':
    main()
