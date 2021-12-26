from typing import Optional
from iv.Binarytree.mytree import MyTree

class TreeNode:
    def __ini__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []

        def traverse(root:TreeNode, num: str):
            if root:
                num += str(root.val)

                if not root.left and not root.right:
                    res.append(num)
                if root.left:
                    traverse(root.left, num)
                if root.right:
                    traverse(root.right, num)
        traverse(root, "")
        # print(res)
        res1 = list(map(self.num_to_binary, res))
        # print(res1)
        return sum(res1)

    def num_to_binary(self, num: str):
        res = 0
        for i in num:
            res = res * 2 + int(i)
        return res


root = [1,0,1,0,1,0,1]
root = [0]
t = MyTree()
rr = t.maketree(root)

s = Solution()
# print(s.num_to_binary("100"))
print(s.sumRootToLeaf(rr))



