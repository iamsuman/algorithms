# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_list(A):
    root = ListNode(A[0])
    temp = root
    for i in A[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    return root


class Solution():
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        if not A:
            return None

            # Move the two pointers until they reach the proper starting point
            # in the list.
        cur, prev = A, None
        while B > 1:
            prev = cur
            cur = cur.next
            B, C = B - 1, C - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while C:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            C -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            A = prev
        tail.next = cur
        return A

    def printlist(self, A):
        root = A
        while root:
            print(root.val)
            root = root.next


A = [1, 2, 3, 4, 5]
m = 2
n = 4

root = make_list(A)
s = Solution()
a = s.reverseBetween(root, m, n)
s.printlist(a)
