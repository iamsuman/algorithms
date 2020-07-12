class Balance():
    def balanced_parenthesis(self, A):
        # n = len(A)
        s = []
        _open = 0
        _close = 0
        for i in A:
            if i in "({[":
                s.append(i)
                _open = _open + 1

            if i in ")}]":
                _close = _close + 1
                if _open < _close:
                    break
                if len(s) > 0:
                    top = s[-1]
                else:
                    top = None
                if (i == ")" and top == "(") or (i == "}" and top == "{") or (i == "]" and top == "["):
                    s.pop(-1)
                else:
                    return 0
            # print("{} and {}".format(i,s))


        # print(s)
        if len(s) > 0 or _open != _close:
            return 0
        else:
            return 1


A = "()()"
A = "(())"
# A = "(()"
A = "()[]{}"
# A = "([)]"
A = "]}"
A = "{}}({})}}[}][({])[[}{{"
A = "{}}"
A = "((((([{()}[]]]{{{[]}}})))))"
a = Balance()
print(a.balanced_parenthesis(A))







