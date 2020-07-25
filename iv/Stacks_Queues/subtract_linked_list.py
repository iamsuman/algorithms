class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

def make_list(A):
    head = ListNode(A[0])
    ptr = head
    for i in A[1:]:
        ptr.next = ListNode(i)
        ptr = ptr.next
    return head


class SubtractList():
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        s, ptr = A, A

        prev = None
        revA = rev(A)
        myA = None

        while A and revA:
            if not myA:
                x = revA.val - A.val
                myA = ListNode(x)
                final = myA
            myA = ListNode(x)

            A = A.next
            revA = revA.next
            myA = myA.next
        return final


def rev(A):
    B = A
    prev = None
    C = B
    while B:
        temp = B
        B = B.next
        temp.next = prev
        prev = temp
    return prev

def display(head):
    L = []
    while head.next:
        L.append(head.val)
        head = head.next
    L.append(head.val)
    print(L)

A = [1,2,3,4,5]
a = make_list(A)
display(a)
s = SubtractList()
# r = s.rev(a)
# display(r)
# display(a)

f = s.subtract(a)
display(f)



