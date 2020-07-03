from functools import cmp_to_key
def mysort(x, y):
    A = int(str(x) + str(y))
    B = int(str(y) + str(x))
    if A > B:
        return x, y
    else:
        return y, x


class Largest():
    def largest_number(self, A):
        for i in range(len(A) - 1):
            for j in range(i+1, len(A)):
                A[i], A[j]= mysort(A[i], A[j])
                # print(type(mysort(A[i], A[j])))
        return "".join(map(str,A))

    def largest_number2(self, A):
        A = list(map(str, A))

        mykey = cmp_to_key(lambda x, y: 1 if x + y > y + x else -1)
        A.sort(key=mykey, reverse=True)
        return "".join(A)





A = [3, 30, 34, 5, 9]
A = [ 12, 121 ]
# A = [ 9, 99, 999, 9998, 9999 ]
a = Largest()
# mynum = a.largest_number2(A)
mynum = a.largest_number2(A)
print(mynum)


