class MyStack:
    def __init__(self, x):
        self.val = x
        self.next = None

class Rev():
    # @param A : string
    # @return a strings
    def reversestring(self, A):
        s = []
        ret = []
        for i in A:
            s.append(i)
        for i in range(len(A)):
            ret.append(s.pop())

        return "".join(ret)

A = "abc"
r = Rev()
print(r.reversestring(A))



