"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def make_tree(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        root.left = make_tree(arr, root.left, 2 * i + 1, n)
        root.right = make_tree(arr, root.right, 2 * i + 2, n)

    return root

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        elif (p.val < root.val < q.val) or (p.val > root.val > q.val):
            return root
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)




root = [6,2,8,0,4,7,9,null,null,3,5]
p = 2
q = 8

