# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list(A):
    if len(A) == 0:
        return None
    head = ListNode(A[0])
    ptr = head
    for i in A[1:]:
        ptr.next = ListNode(i)
        ptr = ptr.next
    return head

def display(head):
    if not head:
        return []
    L = []
    while head.next:
        L.append(head.val)
        head = head.next
    L.append(head.val)
    print(L)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = l1
        prev = None
        while l1 and l2:
            if l1.val <= l2.val:
                if prev:
                    prev.next = l1
                    temp1 = l1.next
                    l1 = temp1
                    prev = prev.next
                    prev.next = l1
                else:
                    prev = l1
                    l1 = l1.next
            else:
                if prev:
                    prev.next = l2
                    temp2 = l2.next
                    l2 = temp2
                    prev = prev.next
                    prev.next = l1
                else:
                    prev = l2
                    res = l2
                    l2 = l2.next
        if l2:
            if prev:
                prev.next = l2
            else:
                res = l2
        if l1:
            if prev:
                prev.next = l1
            else:
                res = l1
        return res


l1 = [1,3,5]; l2 = [2,4,6]
# l1 = [1,2,4]; l2 = [1,3,4]
# l1 = []; l2 = []
# l1 = []; l2 = [0]
# l1 = [0]; l2 = []
# l1 = [2]; l2 = [1]
# l1 = [-9,-7,-6,-1,0,1,2,4,7]; l2 = [-10,-6,4,6,8]

ll1 = make_list(l1)
ll2 = make_list(l2)
s = Solution()
head = s.mergeTwoLists(ll1, ll2)
display(head)






