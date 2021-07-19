# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list(arr):
    head = ListNode(arr[0])
    temp = head
    for i in range(1, len(arr) -1):
        # print(i, head.val)
        head.next = ListNode(arr[i])
        head = head.next
    return temp


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = head

        while head and head.next:
            if head.next.val == head.val:
                t = head.next.next
                head.next = t
            else:
                head = head.next

        return temp


head = [1,1,2,3,3,3]
# head = [1,1,1,1,1]
hh = make_list(head)
s = Solution()
res = s.deleteDuplicates(hh)
while res:
    print(res.val, end=" ")
    res = res.next





