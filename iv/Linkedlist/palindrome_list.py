# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None


def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head


class Palindrom():
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        fast, slow = A, A
        rev = None
        flag = 1
        if not A:
            return True
        while fast and fast.next:
            if not fast.next.next:
                flag = 0
                break
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = rev
            rev = temp
        # print(fast.val)
        fast = slow.next
        slow.next = rev
        if flag:
            slow = slow.next

        # print("fast")
        # myprint(fast)
        # myprint(slow)
        # myprint(A)

        while fast and slow:
            if fast.val != slow.val:
                return 0
            fast = fast.next
            slow = slow.next
        return 1


def myprint(x):
    while x.next:
        print(x.val, end=" ")
        x = x.next
    print(x.val)



A = [1,2,3,2,1]
A = [1,2,3,4,5]
A = [1,2,3,3,2,1]

x = make_list(A)
y = Palindrom()
print(y.lPalin(x))

