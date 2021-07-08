# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, root, res):
        if root:
            res.append(root.val)
        else:
            return []
        if root.left:
            self.traversal(root.left, res)
        if root.right:
            self.traversal(root.right, res)


t = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)

# t = None

s = Solution()
print(s.preorderTraversal(t))
