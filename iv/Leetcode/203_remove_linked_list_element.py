# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(A):
    head = ListNode(A[0])
    ptr = head
    for i in A[1:]:
        ptr.next = ListNode(i)
        ptr = ptr.next
    return head

def display(head):
    L = []
    while head:
        L.append(head.val)
        head = head.next
    print(L)

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        first = ListNode(0)
        first.next = head

        prev, curr = first, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return first.next


A = [1, 2, 3, 4, 5, 6]
B = 2

A = [1]
B = 1
s = Solution()
head = make_list(A)
head1 = s.removeElements(head, B)
display(head1)
