from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        self.res = False

        def traverse(node: TreeNode, summ):
            if node:
                summ += node.val
            if node.left or node.right:
                if node.left:
                    traverse(node.left, summ)
                    # summ -= node.left.val
                if node.right:
                    traverse(node.right, summ)
                    # summ -= node.right.val
            else:
                print(summ)
                if summ == targetSum:
                    self.res = True
            return self.res

        summ = 0
        res = traverse(root, summ)
        return res


root = [5,4,8,11,"null",13,4,7,2,"null","null","null",1]; targetSum = 22
root = [1,2,3]; targetSum = 5
root = [1,2]; targetSum = 0
root = []; targetSum = 1
root = [0,1,1]; targetSum= 0

t = MyTree()
rr = t.maketree(root)

s = Solution()
print(s.hasPathSum(rr, targetSum))
