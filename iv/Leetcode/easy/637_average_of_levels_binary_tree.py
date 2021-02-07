from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> list:
        res = []
        mystack = [root]
        while mystack:
            summ = 0
            tempstack = []
            n = len(mystack)
            for node in mystack:
                summ += node.val
                if node.left:
                    tempstack.append(node.left)
                if node.right:
                    tempstack.append(node.right)
            res.append(summ/n)
            mystack = []
            mystack.extend(tempstack)
        return res


tt1 = [3,9,20,"null", "null", 15,7]
# tt1 = []; tt2 = [1]
t = MyTree()
t1 = t.maketree(tt1)
# print(t.print_tree(t1))

s = Solution()
print(s.averageOfLevels(t1))
