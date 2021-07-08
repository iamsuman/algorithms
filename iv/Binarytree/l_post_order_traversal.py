# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, root, res: list):
        if not root:
            return None
        if root.left:
            self.traversal(root.left, res)
        if root.right:
            self.traversal(root.right, res)
        res.append(root.val)


# Array = [1, null,2,3]
t = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)

s = Solution()
print(s.traversal(t))
