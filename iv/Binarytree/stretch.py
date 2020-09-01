class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Stretch():
    def stretched(self, root, k):
        dummy = Tree(0)
        dummy.left = root
        temp = dummy
        # self.fnc(temp, k)
        return dummy.left

    # def fnc(self, root, k):
    #     if not root:
    #         return None
        # if root.left:
        #     value = int(root.left.val / k)
        #     x = root.left.left
        #     i = 0
        #     while i < k:
        #         root.left = Tree(value)
        #         root = root.left
        #         i += 1
        #     root.left = x
        #     self.fnc(root.left, k)
        # if root.right:
        #     value = int(root.right.val / k)
        #     x = root.right.right
        #     i = 0
        #     while i < k:
        #         root.right = Tree(value)
        #         root = root.right
        #         i = i + 1
        #     root.right = x
        #     self.fnc(root.right, k)


head = Tree(12)
head.left = Tree(81)
head.right = Tree(34)

s = Stretch()
s.stretched(head, 2)
# print(head1.val)
