# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    ans = 1

    def findDepth(self, node, depth):
        if (node == None):
            return depth - 1
        lt_dt = self.findDepth(node.left, depth + 1)
        rt_dt = self.findDepth(node.right, depth + 1)
        if (abs(lt_dt - rt_dt) > 1):
            self.ans = 0
        return max(lt_dt, rt_dt)

    def isBalanced(self, A):
        self.findDepth(A, 0)
        return self.ans

    def make_tree(self, A, root, i, n):
        if i < n:
            temp = TreeNode(A[i])
            root = temp

            root.left = self.make_tree(A, root.left, 2 * i + 1, n)
            root.right = self.make_tree(A, root.right, 2 * i + 2, n)

        return root


A = [1, 2, 3]
A = [100, 98, 102, 96, 99, 97 ]
s = Solution()
root = s.make_tree(A, None, 0, len(A))
res = s.isBalanced(root)
print(res)
