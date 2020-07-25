class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def make_tree(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = make_tree(arr, root.left, 2 * i + 1, n)
        root.right = make_tree(arr, root.right, 2 * i + 2, n)
    return root


class Ksmall(object):
    def kthSmallest(self, root, k):
        nodes = []
        self.solve(root, nodes)
        return nodes[k - 1]

    def solve(self, root, nodes):
        if root == None:
            return
        self.solve(root.left, nodes)
        nodes.append(root.val)
        self.solve(root.right, nodes)


ob1 = Ksmall()
A = [10, 5, 15, 2, 7, 13]
B = 3

A = [1, -1, -1]
B = 1

tree = make_tree(A, A[0],0, len(A))
print(ob1.kthSmallest(tree, B))
