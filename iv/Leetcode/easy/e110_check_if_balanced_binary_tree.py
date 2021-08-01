# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) < 2 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)

    def depth(node: TreeNode):
        if not node:
            return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1
