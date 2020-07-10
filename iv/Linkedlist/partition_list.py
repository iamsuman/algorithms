class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def make_list(A):
    head = ListNode(A[0])
    ptr = head
    for element in A[1:]:
        ptr.next = ListNode(element)
        ptr = ptr.next
    return head

def display(head):
    L = []
    while head.next:
        L.append(head.val)
        head = head.next
    L.append(head.val)
    print(L)

class Partition_list:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        low, hi = None, None
        mylow, myhi = None, None

        var = A
        while var:
            if var.val < B:
                if not low:
                    low = var
                    mylow = low
                else:
                    low.next = var
                    low = low.next
            else:
                if not hi:
                    hi = var
                    myhi = hi
                else:
                    hi.next = var
                    hi = hi.next
            var = var.next
        if hi:
            hi.next = None
        if low:
            low.next = None
        if low:
            low.next = myhi
        else:
            mylow = myhi
        return mylow


A = [ 1, 2, 3, 4, 5]
B = 5

A = [1]
B = 1

A = [3]
B = 5

A = [ 384, 183, 463, 31 ]
B = 77

head = make_list(A)
a = Partition_list
ret = a.partition(a, head, B)
display(ret)


