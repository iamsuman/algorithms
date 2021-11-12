from iv.Binarytree.mytree import MyTree
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        maxm = max(nums)
        ind = nums.index(maxm)
        root = TreeNode(maxm)

        root.left = self.constructMaximumBinaryTree(nums[:ind])
        root.right = self.constructMaximumBinaryTree(nums[ind+1:])

        return root


nums = [3,2,1,6,0,5]
# nums = [3,2,1]
s = Solution()
root = s.constructMaximumBinaryTree(nums)
t = MyTree()
res = t.print_tree(root)
print(res)

