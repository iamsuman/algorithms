# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        res = []

        def Traversal(root, res):
            if root:
                res.append(root.val)
                print(root.val)

            else:
                return []
            if root.left:
                Traversal(root.left, res)
            if root.right:
                Traversal(root.right, res)


        Traversal(root, res)
        return res

t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

s = Solution()
print(s.levelOrder(t))
