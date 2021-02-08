from iv.Binarytree.mytree import MyTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        mystack = []

        def find(root: TreeNode, k: int, mystack: list):
            if root is None:
                return False
            if (k - root.val) in mystack:
                return True
            mystack.append(root.val)
            return find(root.left, k, mystack) or find(root.right, k, mystack)

        return find(root, k, mystack)


root = [5,3,6,2,4,"null",7]; k = 9
# root = [5, 3, 6, 2, 4, "null", 7]; k = 28
t = MyTree()
root1 = t.maketree(root)
s = Solution()
print(s.findTarget(root1, k))
