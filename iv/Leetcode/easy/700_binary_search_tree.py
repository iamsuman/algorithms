from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def traverse(root: TreeNode, val: int):
            if not root:
                return None
            if root.val == val:
                return root
            elif root.val > val:
                return traverse(root.left, val)
            else:
                return traverse(root.right, val)

        return traverse(root, val)


root = [4,2,7,1,3]; val = 2
root = [4,2,7,1,3]; val = 5
m = MyTree()
mt = m.maketree(root)
s = Solution()
print(s.searchBST(mt, val))
