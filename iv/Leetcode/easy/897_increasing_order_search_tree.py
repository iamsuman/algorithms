from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        temp_list = []
        def traverse(root: TreeNode):
            if root:
                if root.left:
                    traverse(root.left)
                temp_list.append(root.val)
                if root.right:
                    traverse(root.right)
        traverse(root)
        print(temp_list)

        rr = TreeNode(temp_list[0])
        res = rr
        for value in temp_list[1:]:
            rr.right = TreeNode(value)
            rr = rr.right

        return res


root = [5,3,6,2,4,"null",8,1,"null","null","null",7,9]
root = [5,1,7]
t = MyTree()
rr = t.maketree(root)
s = Solution()
res = s.increasingBST(rr)
print(t.print_tree(res))







