from typing import List
from iv.Binarytree.mytree import MyTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]

        def traversal(mystack: List[TreeNode]):
            l = []
            for node in mystack:
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            if len(l) == 0:
                return
            r = list(map(lambda x: x.val, l))
            res.append(r)
            traversal(l)

        traversal([root])
        return res


root = [3,9,20,"null","null",15,7]
t = MyTree()
rr = t.maketree(root)
s = Solution()
print(s.levelOrder(rr))

