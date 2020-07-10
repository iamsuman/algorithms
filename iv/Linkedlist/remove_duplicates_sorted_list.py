# Definition for singly-linked list.
class ListNode:
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

def display(head):
    L = []
    while head.next:
        L.append(head.val)
        head = head.next
    L.append(head.val)
    print(L)


class Remove():
    # @param A : head node of linked list
    # @return the head node in the linked list
    def delete_duplicates(self, A):
        ret = A
        ptr = ret
        while A:
            if A.next:
                if A.next.val == A.val:
                    A = A.next
                    continue
            ret.next = A.next
            A = A.next
            ret = ret.next
        return ptr


A = [1, 1, 2, 3, 3, 4]
A = [1, 1, 2, 3, 3, 4, 4, 4, 4]
head = make_list(A)
display(head)
a = Remove()
rev = a.delete_duplicates(head)
display(rev)
