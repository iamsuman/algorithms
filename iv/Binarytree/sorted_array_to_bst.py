class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if not A:
            return None
        mid = int(len(A)/2)
        root = TreeNode(A[mid])
        root.left = self.sortedArrayToBST(A[:mid])
        root.right = self.sortedArrayToBST(A[mid+1:])
        return root

    def insert_bst(self, root, key):
        if root is None:
            return TreeNode(key)

        if root.val > key:
            root.left = self.insert_bst(root.left, key)
        else:
            root.right = self.insert_bst(root.right, key)
        return root


A = [1, 2, 3]


c = Solution()
root = c.sortedArrayToBST(A)
print(root)

