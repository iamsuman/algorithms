from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        res = []
        self.traversal2(root, res)
        return res

    def traversal(self, root, res):
        # Morris
        pass

    def traversal2(self, root: TreeNode, res: list):
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        if root:
            if root.left:
                self.traversal2(root.left, res)
            res.append(root.val)
            if root.right:
                self.traversal2(root.right, res)


t = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)

# t = None

s = Solution()
print(s.inorderTraversal(t))



