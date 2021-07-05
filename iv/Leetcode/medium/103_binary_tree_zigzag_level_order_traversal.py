# Definition for a binary tree node.
from typing import List
from iv.Binarytree.mytree import MyTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        order = 1

        def traverse(order, mystack: List[TreeNode]):
            l = []
            for node in mystack:
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            if len(l) == 0:
                return
            r = list(map(lambda x: x.val, l))
            if order == 1:
                res.append(r)
            else:
                res.append(r[::-1])
            order = order * -1
            traverse(order, l)

        traverse(-1, [root])
        return res


root = [3,9,20,"null","null",15,7]
root = [1]
root = []
t = MyTree()
rr = t.maketree(root)
s = Solution()
print(s.zigzagLevelOrder(rr))









