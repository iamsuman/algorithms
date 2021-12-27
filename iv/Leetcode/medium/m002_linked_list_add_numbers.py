"""
Add two numbers represented as linked list
"""
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l = ListNode()
        res = l

        while l1 and l2:
            v = l1.val + l2.val + carry
            if v > 9:
                v -= 10
                carry = 1
            else:
                carry = 0
            l.next = ListNode(v)
            l = l.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            v = l1.val + carry
            if v > 9:
                v -= 10
                carry = 1
            else:
                carry = 0
            l.next = ListNode(v)
            l = l.next
            l1 = l1.next
        while l2:
            v = l2.val + carry
            if v > 9:
                v -= 10
                carry = 1
            else:
                carry = 0
            l.next = ListNode(v)
            l = l.next
            l2 = l2.next

        if carry == 1:
            l.next = ListNode(1)

        return res.next

    def create_linked_list(self, arr: List[int]):
        l = ListNode()
        res = l
        for i in arr:
            l.next = ListNode(i)
            l = l.next
        return res.next

    def print_linkedin_list(self, l: ListNode):
        arr = []
        while l:
            arr.append(l.val)
            l = l.next
        return arr


l1 = [2,4,3]; l2 = [5,6,4]
l1 = [0]; l2 = [0]
l1 = [9,9,9,9,9,9,9]; l2 = [9,9,9,9]
s = Solution()
ll1 = s.create_linked_list(l1)
ll2 = s.create_linked_list(l2)
res = s.addTwoNumbers(ll1, ll2)
print(s.print_linkedin_list(res))
