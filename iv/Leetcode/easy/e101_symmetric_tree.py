from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        depth_stack = [root]
        while len(depth_stack) > 0:
            temp_stack = []
            for node in depth_stack:
                # print(node.val)
                if node and node.left:
                    temp_stack.append(node.left)
                else:
                    temp_stack.append(None)
                if node and node.right:
                    temp_stack.append(node.right)
                else:
                    temp_stack.append(None)
            if len(temp_stack) == temp_stack.count(None):
                temp_stack = []
            if self.validate_symmetric(temp_stack):
                depth_stack = [node for node in temp_stack]
            else:
                return False
        return True

    def validate_symmetric(self, d_stack: List[TreeNode]):
        lo, hi = 0, len(d_stack) - 1
        while lo <= hi:
            if d_stack[lo] is None or d_stack[hi] is None:
                if d_stack[lo] != d_stack[hi]:
                    return False
            elif d_stack[lo].val != d_stack[hi].val:
                return False
            lo += 1
            hi -= 1
        return True

    def isSymmetric2(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return t1.val == t2.val and \
               self.isMirror(t1.right, t2.left) and \
               self.isMirror(t1.left, t2.right)


root = [1,2,2,3,4,4,3]
# root = [1,2,2,"null",3,"null",3]
# root = [1]
# root = [1,2,2,"null",3,3]
t = MyTree()
rr = t.maketree(root)
s = Solution()
print(s.isSymmetric(rr))
print(s.isSymmetric2(rr))


