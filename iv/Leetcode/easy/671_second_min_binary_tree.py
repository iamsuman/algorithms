from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = []

        def traverse(root: TreeNode):
            if root:
                res.append(root.val)
                if root.left:
                    traverse(root.left)
                if root.right:
                    traverse(root.right)

        traverse(root)
        res = list(set(res))
        # print(res)

        res.sort()
        if len(res) < 2:
            return -1
        else:
            return res[1]


root = [2, 2, 5, "null", "null", 5, 7]
# root = [2, 2, 5]
# root = [2,2,2]
root = [2,2,5,"null","null",5,5]
root = [2]
root = []
root = [1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]
t = MyTree()

t1 = t.maketree(root)

s = Solution()
print(s.findSecondMinimumValue(t1))



