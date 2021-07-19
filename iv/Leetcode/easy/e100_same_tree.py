from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)


p = [1,2,3]; q = [1,2,3]
p = [1,2]; q = [1,"null",2]
p = [1,2,1]; q = [1,1,2]
t = MyTree()
pp = t.maketree(p)
qq = t.maketree(q)
s = Solution()
print(s.isSameTree(pp, qq))
