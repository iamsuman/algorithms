from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        mindepth = 10 ** 5

        def traversal(node: TreeNode, depth, mindepth):
            if node:
                depth += 1
                if not node.left and not node.right:
                    if mindepth > depth:
                        mindepth = depth
                        return mindepth
                if node.left:
                    mindepth = min(traversal(node.left, depth, mindepth), mindepth)
                if node.right:
                    mindepth = min(traversal(node.right, depth, mindepth), mindepth)
            return mindepth

        return traversal(root, 0, mindepth)


root = [3,9,20,"null","null",15,7]
root = [2,"null",3,"null",4,"null",5,"null",6]
t = MyTree()
rr = t.maketree(root)

s = Solution()
print(s.minDepth(rr))
