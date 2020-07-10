class ListNode:
    def __init__(self, x):
       self.val = x
       self.next = None


def rev_linked_list(head):
    prev = None
    while head:
        temp = head
        head = head.next
        temp.next = prev
        prev = temp
    return prev


def make_list(A):
    head = ListNode(A[0])
    ptr = head
    for i in A[1:]:
        ptr.next = ListNode(i)
        ptr = ptr.next
    return head


def display(head):
    L = []
    while head.next:
        L.append(head.val)
        head = head.next
    L.append(head.val)
    print(L)


A = [1,2,3,4,5]
mylinkedlist = make_list(A)
display(mylinkedlist)
rev = rev_linked_list(mylinkedlist)
display(rev)




