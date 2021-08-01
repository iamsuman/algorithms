from typing import List

from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def make_bst(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            root = TreeNode(nums[mid])
            root.left = make_bst(lo, mid - 1)
            root.right = make_bst(mid + 1, hi)
            return root

        return make_bst(0, len(nums) -1)


nums = [-10,-3,0,5,9]
nums = [1,3]
s = Solution()
root = s.sortedArrayToBST(nums)
t = MyTree()
print(t.print_tree(root))



