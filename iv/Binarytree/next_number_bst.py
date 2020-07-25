# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_bst(arr):
    root = None
    for k in arr:
        root = insert_bst(root, k)
    return root


def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        a =  self.search(A, None, B)
        return a

    def search(self, root: TreeNode, succ, B):
        if root is None:
            return None

        if root.val == B:
            if root.right:
                return self.findmin(root.right)
        if root.val > B:
            succ = root
            return self.search(root.left, succ, B)
        if root.val < B:
            return self.search(root.right, succ, B)
        return succ

    def findmin(self, root):
        while root.left:
            root = root.left
        return root

    def findSuccessor(self, root, key):

        succ = None

        while True:

            # if given key is less than the root node, visit left subtree
            if key < root.val:
                # update successor to current node before visiting
                # left subtree
                succ = root
                root = root.left

            # if given key is more than the root node, visit right subtree
            elif key > root.val:
                root = root.right

            # if node with key's value is found, the successor is minimum
            # value node in its right subtree (if any)
            else:
                if root.right:
                    succ = self.findmin(root.right)
                break

            # if key doesn't exist in binary tree
            if root is None:
                return None

        # return Successor if any
        return succ


A = [100, 98, 102, 96, 99, 97]
B = 97

A = [15, 10, 20, 8, 12, 16, 25]
B = 8

A = "31 19 34 13 25 -1 97 7 16 22 28 64 112 4 10 -1 -1 -1 -1 -1 -1 37 67 100 160 1 -1 -1 -1 -1 52 -1 73 -1 106 124 175 -1 -1 46 61 70 79 103 109 121 145 169 220 43 49 55 -1 -1 -1 76 88 -1 -1 -1 -1 115 -1 139 151 166 172 181 226 40 -1 -1 -1 -1 58 -1 -1 85 94 -1 118 133 142 148 157 163 -1 -1 -1 178 205 223 -1 -1 -1 -1 -1 82 -1 91 -1 -1 -1 127 136 -1 -1 -1 -1 154 -1 -1 -1 -1 -1 193 211 -1 -1 -1 -1 -1 -1 -1 130 -1 -1 -1 -1 190 202 208 214 -1 -1 187 -1 196 -1 -1 -1 -1 217 184 -1 -1 199 -1 -1 -1 -1 -1 -1".split()
A = map(int, A)
B = 13

root = make_bst(A)
# print(root)
s = Solution()
# next_node = s.getSuccessor(root, B)
# print(next_node.val)

next_node = s.findSuccessor(root, B)
print(next_node.val)


