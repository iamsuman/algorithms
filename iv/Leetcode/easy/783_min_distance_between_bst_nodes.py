from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        mylist = []
        def traverse(root):
            if root:
                if root.left:
                    traverse(root.left)
                mylist.append(root.val)
                if root.right:
                    traverse(root.right)

        traverse(root)
        min_dist = max(mylist)
        for i in range(len(mylist) - 1):
            if abs(mylist[i] - mylist[i+1]) < min_dist:
                min_dist = abs(mylist[i] - mylist[i+1])
        return min_dist


root = [4,2,6,1,3]
root = []
root = [1,0,48,"null","null",12,49]
mt = MyTree()
root_bst = mt.maketree(root)
s = Solution()
print(s.minDiffInBST(root_bst))
