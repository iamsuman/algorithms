# Definition for a  binary tree node
class TreeNode:
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

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val,end=" ")
        inOrder(root.right)

class ValidBST():
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        INT_MAX = 4294967296
        INT_MIN = -4294967296
        if self.isValidBSTUtil(A, INT_MIN, INT_MAX):
            return 1
        else:
            return 0
        # return self.isValidBSTUtil(A, INT_MIN, INT_MAX)

    def isValidBSTUtil(self, node: TreeNode, minvalue, maxvalue):
        if node is None:
            return True
        if node.val < minvalue or node.val > maxvalue:
            return False
        return (self.isValidBSTUtil(node.left, minvalue, node.val - 1)
                and
                self.isValidBSTUtil(node.right, node.val + 1, maxvalue))




A = [1,2,3,4,5]
A = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6]

A = [1,2,3]

A = list(map(int, "4 2 5 1 5 -1 -1 -1 -1 -1 -1".split(" ")))

A = "91 -1 -1".split(" ")
A = list(map(int, A))
root = make_tree(A, None, 0, len(A))
# inOrder(root)
# print(root.left.val)

a = ValidBST()
print(a.isValidBST(root))
