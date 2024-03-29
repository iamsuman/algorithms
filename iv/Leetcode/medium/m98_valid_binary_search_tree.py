import math
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        right = float("inf")
        left = -1 * right

        def traverse(root: TreeNode, left, right):
            if not root:
                return True
            if not (left < root.val < right):
                return False
            return traverse(root.left, left, root.val) and traverse(root.right, root.val, right)

        return traverse(root, left, right)



    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        lstatus = True
        rstatus = True
        if root:
            if root.left:
                if root.val < root.left.val:
                    lstatus = False
                else:
                    lstatus = self.isValidBST(root.left)
            if root.right:
                if root.val > root.right.val:
                    rstatus = False
                else:
                    rstatus = self.isValidBST(root.right)
        return lstatus and rstatus

    def isValidBST3(self, root: Optional[TreeNode]) -> bool:

        res = []
        def traverse(root: TreeNode):
            if root:
                if root.left:
                    traverse(root.left)
                res.append(root.val)
                if root.right:
                    traverse(root.right)
        traverse(root)
        if len(res) == 1:
            return True
        for i in range(len(res) -1):
            if res[i] > res[i+1]:
                return False
        return True






