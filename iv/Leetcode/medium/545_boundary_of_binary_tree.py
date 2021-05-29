# Definition for a binary tree node.
from typing import List
from iv.Binarytree.mytree import MyTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        res = []
        depth = []
        lt = []
        rt = []

        def traversal(mystack: List[TreeNode]):
            temp = []
            for node in mystack:
                if node.left:
                    temp.append(node.left)
                    lt.append(node.left)
                if node.right:
                    temp.append(node.right)
                    rt.append(node.right)
            if temp:
                depth.append(temp)
                t = list(map(lambda x: x.val, temp))
                res.append(t)
                traversal(temp)


        depth.append([root])
        lt.append(root)
        res = [[root.val]]
        traversal([root])
        print(res)

        ll = []
        rr = []
        mid = []
        d = len(depth)
        for i in range(d):
            print(list(map(lambda x: x.val, depth[i])))
            len_d = len(depth[i])
            if len_d == 1:
                if depth[i][0] in lt:
                    ll.append(depth[i][0].val)
                if depth[i][-1] in rt:
                        rr.append(depth[i][-1].val)
            else:
                ll.append(depth[i][0].val)
                for node in depth[i][1:len_d-1]:
                    if not node.left and not node.right:
                        mid.append(node.val)
                rr.append(depth[i][-1].val)
        ans = ll + mid + rr[::-1]
        return ans


root = [1,"null",2,3,4]
root = [1,2,3,4,5,6,"null","null","null",7,8,9,10]
root = [1,2,7,3,5,"null",6,4]
root = [3,2,"null","null",4,1]
t = MyTree()
rr = t.maketree(root)
s = Solution()
print(s.boundaryOfBinaryTree(rr))




