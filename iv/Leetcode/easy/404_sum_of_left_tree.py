"""
Find sum of the left nodes of a binary tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.summ = 0
        self.traversal(root)
        return self.summ

    def traversal(self, root):
        if root.left:
            if root.left.left is None and root.left.right is None:
                # print(root.left.val)
                self.summ += root.left.val
                # summ += root.left.val
            else:
                self.traversal(root.left)
        if root.right:
            self.traversal(root.right)

    def make_tree(self, A, root, i, n):
        if i < n:
            # print(A[i])
            temp = TreeNode(A[i])
            root = temp

            root.left = self.make_tree(A, root.left, 2 * i + 1, n)
            root.right = self.make_tree(A, root.right, 2 * i + 2, n)

        return root


A = [3,9,20,8,0, 15, 7]
A = [-9,-3,2,None,4,4,0,-6,None,-5]
s = Solution()
root = s.make_tree(A, A[0], 0, len(A))

root = TreeNode(-9)
root.left = TreeNode(-3)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(0)

root.left.right.left = TreeNode(-6)
root.right.left.left = TreeNode(-5)
print(s.sumOfLeftLeaves(root))
