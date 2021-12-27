from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []

        def traverse(root:TreeNode):
            if root:
                if root.left:
                    traverse(root.left)
                res.append(root)
                if root.right:
                    traverse(root.right)
        traverse(root)
        # print(list(map(lambda x: x.val, res)))
        notfound = True
        node1 = None
        node2 = None
        ind = []
        for i in range(len(res)):
            if notfound:
                # print(res[i].val, res[i+1].val)
                if res[i].val > res[i+1].val:
                    node1 = res[i]
                    notfound = False
            else:
                if res[i].val < res[i - 1].val:
                    ind.append(i)
        # print(ind)
        node2 = res[max(ind)]
        # print(node1.val, node2.val)
        node1.val, node2.val = node2.val, node1.val


t = TreeNode(3)
t.left = TreeNode(1); t.right = TreeNode(4); t.right.left = TreeNode(2)

t = TreeNode(1); t.left = TreeNode(3); t.left.right = TreeNode(2)

obj = MyTree()

root = [1,3,"null","null",2]
# root = [3,1,4,"null","null",2]
t = obj.maketree(root)
s = Solution()
s.recoverTree(t)
print(obj.print_tree(t))


