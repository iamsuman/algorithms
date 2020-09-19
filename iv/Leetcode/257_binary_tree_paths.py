"""
Given a binary tree, return all root-to-leaf paths.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # TODO check again
        def create_path(root, path):
            if root:
                path = path + str(root.val)
                if not root.left and not root.right: # reached Leaf
                    paths.append(path)
                else:
                    path += "->"
                    create_path(root.left, path)
                    create_path(root.right, path)

        paths = []
        create_path(root, '')
        return paths



t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.right = TreeNode(5)

s = Solution()
print(s.binaryTreePaths(t))






