# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = self.len_list(headA)
        l2 = self.len_list(headB)

        if l1 >= l2:
            p1 = headA
            p2 = headB
        else:
            p1 = headB
            p2 = headA

        c = abs(l1 - l2)
        while c > 0:
            p1 = p1.next
            c -= 1

        while p1:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None

    def len_list(self, p: ListNode):
        l = 0
        while p:
            l += 1
            p = p.next
        return l

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = headA
        while A:
            B = headB
            while B:
                if A.val == B.val:
                    return A
                B = B.next
            A = A.next
        return None

    def make_linked_list(self, arr: List[int]):
        if len(arr) == 0:
            h = None
        else:
            h = ListNode(arr[0])
            hh = h
            for i in range(1, len(arr)):
                hh.next = ListNode(arr[i])
                hh = hh.next
        return h


intersectVal = 8; listA = [4,1,8,4,5]; listB = [5,6,1,8,4,5]; skipA = 2; skipB = 3
s = Solution()
A = s.make_linked_list(listA)
B = s.make_linked_list(listB)
res = s.getIntersectionNode(A, B)
if res:
    print(res.val)




