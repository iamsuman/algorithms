"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
 A =  5 -> 8 -> 20
 B = 4 -> 11 -> 15
 result = 4 -> 5 -> 8 -> 11 -> 15 -> 20
"""
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


class Solution():
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A.val <= B.val:
            head = A
            A = A.next
        else:
            head = B
            B = B.next

        temp = head

        while A and B:
            if A.val <= B.val:
                temp.next = A
                temp = temp.next
                A = A.next
            else:
                temp.next = B
                temp = temp.next
                B = B.next
        if A:
            temp.next = A

        if B:
            temp.next = B

        return head


A = [5, 8, 20]
B = [4, 11, 15]
AA = make_list(A)
BB = make_list(B)

s = Solution()
head = s.mergeTwoLists(AA,BB)


