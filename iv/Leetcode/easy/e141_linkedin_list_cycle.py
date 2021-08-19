# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        if not head.next:
            return False
        while slow and fast:
            if slow == fast:
                return True
            if slow.next and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                break
        return False


head = [3,2,0,-4]; pos = 1
head = [1,2]; pos = 0
head = [1]; pos = -1
head = []; pos = -1
h = ListNode(3); h.next = ListNode(2); h.next.next = ListNode(0);
h.next.next.next = ListNode(-4); h.next.next.next.next = h.next

if len(head) == 0:
    h = None
else:
    h = ListNode(head[0])
    hh = h
    for i in range(1,len(head)):
        hh.next = ListNode(head[i])
        hh = hh.next
    if pos == -1:
        hh.next = None
    else:
        t = h
        while i > 0:
            t = t.next
            i -= 1
        hh.next = t
# print(h.val)
s = Solution()
print(s.hasCycle(h))
