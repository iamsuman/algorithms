from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def isvalid(node: TreeNode):
            if not node:
                return False
            a1 = isvalid(node.left)
            a2 = isvalid(node.right)
            if not a1: node.left = None
            if not a2: node.right = None
            return node.val == 1 or a1 or a2

        return root if isvalid(root) else None


t = MyTree()
mytt = [1,"null",0,0,1]
root = t.maketree(mytt)
s = Solution()
print(s.pruneTree(root))
res = t.print_tree(s.pruneTree(root))
print(res)

