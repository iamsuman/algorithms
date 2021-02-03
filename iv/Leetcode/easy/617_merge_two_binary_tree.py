from iv.Binarytree.mytree import MyTree
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def traversal(root1: TreeNode, root2: TreeNode):
            if root1 and root2:
                root1.val = root1.val + root2.val
                if root1.left and root2.left:
                    traversal(root1.left, root2.left)
                elif root2.left:
                    root1.left = root2.left
                if root1.right and root2.right:
                    traversal(root1.right, root2.right)
                elif root2.right:
                    root1.right = root2.right
            elif root2:
                root1 = root2

        if t1:
            res = t1
        elif t2:
            res = t2
        else:
            return []
        traversal(t1, t2)
        return res


    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        return t1 or t2



tt1 = [1,3,2,5]; tt2 = [2,1,3,"null", 4, "null",7]
tt1 = []; tt2 = [1]
t = MyTree()
t1 = t.maketree(tt1); t2 = t.maketree(tt2)

s = Solution()
res = s.mergeTrees(t1, t2)
print(t.print_tree(res))
