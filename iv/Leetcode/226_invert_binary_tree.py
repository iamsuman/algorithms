class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def invertTree(self, root: Tree):
        head = root

        if not root:
            return None
        temp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp
        return head


t = Tree(4)
t.left = Tree(2)
t.right= Tree(7)
t.left.left = Tree(1)
t.left.right = Tree(3)

s = Solution()
head1 = s.invertTree(t)
print(head1.left.val)

