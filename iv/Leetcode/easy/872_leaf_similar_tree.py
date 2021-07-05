from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def traverse(root: TreeNode, res: list):
            if root.left:
                traverse(root.left, res)
            if root.right:
                traverse(root.right, res)
            if not root.left and not root.right:
                res.append(root.val)

        res1 = []
        res2 = []
        traverse(root1, res1)
        traverse(root2, res2)
        # print(res1)
        # print(res2)
        if res1 == res2:
            return True
        else:
            return False

    def leafSimilar2(self, root1: TreeNode, root2: TreeNode) -> bool:
        res = []

        def traverse(root: TreeNode):
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            if not root.left and not root.right:
                res.append(root.val)

        traverse(root1)
        res1 = [i for i in res]
        res = []
        traverse(root2)
        res2 = [i for i in res]

        # print(res1)
        # print(res2)
        if res1 == res2:
            return True
        else:
            return False


root1 = [3,5,1,6,2,9,8,"null","null",7,4]; root2 = [3,5,1,6,7,4,2,"null","null","null","null","null","null",9,8]
root1 = [1]; root2 = [2]
root1 = [1,2]; root2 = [2,2]
root1 = [1,2,3]; root2 = [1,3,2]
t = MyTree()
rr1 = t.maketree(root1)
rr2 = t.maketree(root2)
s = Solution()
print(s.leafSimilar(rr1, rr2))
print(s.leafSimilar2(rr1, rr2))


