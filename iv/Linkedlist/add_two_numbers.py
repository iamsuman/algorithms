class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_list(A):
    mylist = list(str(A))
    head = ListNode(int(mylist[-1]))
    ptr = head
    for i in mylist[-2::-1]:
        ptr.next = ListNode(int(i))
        ptr = ptr.next
    return head

def display(head):
    L = []
    while head.next:
        L.append(head.val)
        head = head.next
    L.append(head.val)
    print(L)


class MyAdd():
    def add_numbers(self, A, B):
        start = True
        quot = 0
        while A and B:
            mysum = A.val + B.val + quot
            if mysum >= 10:
                rem = mysum % 10
                quot = int(mysum / 10)
            else:
                rem = mysum
            if start:
                lsum = ListNode(rem)
                ret = lsum
                start = False
            else:
                print(rem)
                lsum.next = ListNode(rem)
                lsum = lsum.next

            A = A.next
            B = B.next

        # if quot == 1:
        #     lsum.next = ListNode(quot)
        return ret

A = 342
B = 465
a = make_list(A)
display(a)
b = make_list(B)
display(b)
c = MyAdd()
res = c.add_numbers(a,b)
display(res)

