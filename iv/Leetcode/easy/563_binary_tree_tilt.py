class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        # TODO improve binary tree traversing
        self.summ = 0
        def traversal(root):
            if not root:
                return
            self.summ = self.summ + self.tilt(root)
            if root.left:
                traversal(root.left)
            if root.right:
                traversal(root.right)
        traversal(root)
        return self.summ

    def tilt(self, root: TreeNode) -> TreeNode:
        if not root:
            return 0
        l_sum = self.tree_sum(root.left)
        r_sum = self.tree_sum(root.right)
        tilt = abs(l_sum - r_sum)
        return tilt

    def tree_sum(self, root:TreeNode):
        if not root:
            return 0
        return self.tree_sum(root.left) + self.tree_sum(root.right) + root.val


root = TreeNode(1); root.left = TreeNode(2); root.right = TreeNode(3)

# root = None

root = TreeNode(4); root.left = TreeNode(2); root.right = TreeNode(9)
root.left.left = TreeNode(3); root.left.right = TreeNode(5); root.right.right = TreeNode(7)
s = Solution()
# print(s.tilt(root))
print(s.findTilt(root))

