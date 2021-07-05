# Definition for a binary tree node.
from typing import List
from iv.Binarytree.mytree import MyTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        def traversal(arr: List[TreeNode]):
            temp = []
            for node in arr:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                res.append(list(map(lambda x: x.val, temp)))
                traversal(temp)
        if root:
            res = [[root.val]]
            traversal([root])
        else:
            res = []

        print(res)
        ans = []
        for depth in res:
            ans.append(depth[-1])
        return ans

    def rightSideView2(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            trees = [root]
            res.append(list(map(lambda x: x.val, trees)))
            while trees:
                temp = []
                for tree in trees:
                    if tree.left:
                        temp.append(tree.left)
                    if tree.right:
                        temp.append(tree.right)
                if temp:
                    res.append(list(map(lambda x: x.val, temp)))
                trees = temp
        else:
            return []
        # print(res)
        ans = []
        for node in res:
            ans.append(node[-1])
        return ans


root = [1,2,3,"null",5,"null",4]
# root = [1,"null",3]
# root = []
t = MyTree()
rr = t.maketree(root)
s = Solution()
print(s.rightSideView(rr))

