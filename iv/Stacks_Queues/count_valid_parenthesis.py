class Valid():
    def longest_valid_parenthesis(self, A):
        # n = len(A)
        s = []
        pair = 0
        maxpair = 0

        for i in A:
            if i in "({[":
                s.append(i)
            if i in ")}]":
                if len(s) > 0:
                    top = s[-1]
                else:
                    top = None
                    pair = 0
                if (i == ")" and top == "(") or (i == "}" and top == "{") or (i == "]" and top == "["):
                    s.pop(-1)
                    pair = pair + 1
                    if maxpair < pair:
                        maxpair = pair
                else:
                    pair = 0
                    s = []
        return maxpair * 2



A = "()()"
# A = "(())"
# A = "(()"
A = ")()))(())((())))))())()(((((())())((()())(())((((())))())((()()))(()(((()()(()((()()))(())()))((("
A = ")()))(())((())))))())"
A = "()(((((())())((()())(())((((())))())((()()))(()(((()()(()((()()))(())()))((("
# A = "())"
A = "(()())(())((((())))())((()()))"
A = "()(((((())())((()())(())((((())))())((()()))"
A = "((())())((()())"


# "()(((((())())((()())(())((((())))())((()()))(()(((()()(()((()()))(())()))((("

a = Valid()
print(a.longest_valid_parenthesis(A))







