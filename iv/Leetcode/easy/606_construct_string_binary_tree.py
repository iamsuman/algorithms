# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        res = []

        def traversal(root: TreeNode):
            if root:
                res.append(str(root.val))
                # res = res + str(root.val)
                if root.left or root.right:
                    if root.left:
                        res.append("(")
                        traversal(root.left)
                        res.append(")")
                    else:
                        res.append("()")
                    if root.right:
                        res.append("(")
                        traversal(root.right)
                        res.append(")")
                    # else:
                    #     res.append("()")
        traversal(t)
        return "".join(res)


t = TreeNode(1); t.left = TreeNode(2); t.right = TreeNode(3); t.left.left = TreeNode(4)
# t = TreeNode(1); t.left = TreeNode(2); t.right = TreeNode(3); t.left.right = TreeNode(4)
s = Solution()
print(s.tree2str(t))

