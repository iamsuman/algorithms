from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        values = []

        def traversal(root: TreeNode):
            values.append(root.val)
            if root.left:
                traversal(root.left)
            if root.right:
                traversal(root.right)

        traversal(root)
        if len(set(values)) == 1:
            return True
        else:
            return False

    def isUnivalTree2(self, root: TreeNode) -> bool:
        left_valid = (not root.left or root.val == root.left.val and self.isUnivalTree2(root.left))
        right_valid = (not root.right or root.val == root.right.val and self.isUnivalTree2(root.right))
        return left_valid and right_valid

root = [1,1,1,1,1,"null",1]
# root = [2,2,2,5,2]
t = MyTree()
rr = t.maketree(root)
s = Solution()
print(s.isUnivalTree(rr))
print(s.isUnivalTree2(rr))




