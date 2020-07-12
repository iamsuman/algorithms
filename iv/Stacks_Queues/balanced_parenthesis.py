class Valid():
    def longest_valid_parenthesis(self, A):
        # n = len(A)
        s = []
        open = 0
        close = 0
        count = 0
        maxcount = 0

        for i in A:
            if i == "(":
                open = open + 1
                s.append(i)
            if i == ")":
                if close >= open:
                    close = 0
                    start = 0
                    continue
                else:
                    close = close + 1
                    open = open
                    count = count + 2
                    s.append(i)
            # if count > maxcount:
            #     maxcount = count

        if open == close:
            return 0
        else:
            return 1

A = "()()"
A = "(())"
# A = "(()"
a = Valid()
print(a.longest_valid_parenthesis(A))







