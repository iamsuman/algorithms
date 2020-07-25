class ListNode():
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


class SubtractList():
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        if not A.next:
            return A
        fast = A
        slow = A
        prev = None
        cnt = 0
        # reach till half
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            cnt += 1
        if fast:
            start = slow.next
        else:
            start = slow
        # reverse the latter half
        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp

        firstA = A
        lastA = prev
        prev1 = prev
        currA = A

        # modify values of first half
        while cnt:
            currA.val = lastA.val - firstA.val
            firstA = firstA.next
            lastA = prev.next

            prev = prev.next

            currA = currA.next
            cnt -= 1

        # reverse the list again
        new_prev = None
        while prev1:
            temp = prev1.next
            prev1.next = new_prev
            new_prev = prev1
            prev1 = temp

        return A


def rev(A):
    B = A
    prev = None
    C = B
    while B:
        temp = B
        B = B.next
        temp.next = prev
        prev = temp
    return prev

def display(head):
    L = []
    while head.next:
        L.append(head.val)
        head = head.next
    L.append(head.val)
    print(L)

A = [1,2,3,4,5]
a = make_list(A)
display(a)
s = SubtractList()
# r = s.rev(a)
# display(r)
# display(a)

f = s.subtract(a)
display(f)



