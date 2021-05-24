from iv.Binarytree.mytree import MyTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x1 = []
        y1 = []
        def traversal(node, depth, parent):
            if node:
                depth += 1
                # print(node.val, depth)
                if node.val == x:
                    if parent:
                        x1.append((parent.val, depth))
                    else:
                        x1.append((None, depth))
                if node.val == y:
                    if parent:
                        y1.append((parent.val, depth))
                    else:
                        y1.append((None, depth))


                if node.left:
                    traversal(node.left, depth, node)
                if node.right:
                    traversal(node.right, depth, node)

        traversal(root, 0, None)
        # print(x1)
        # print(y1)
        if x1[0][0] != y1[0][0] and x1[0][1] == y1[0][1]:
            return True
        else:
            return False


root = [1,2,3,4]; x = 4; y = 3
# root = [1,2,3,"null",4,"null",5]; x = 5; y = 4
root = [1,2,3,"null",4]; x = 2; y = 3
root = [1,"null",2,3,"null","null",4,"null",5]; x = 1; y = 3
t = MyTree()
rr = t.maketree(root)
s = Solution()
print(s.isCousins(rr, x, y))
