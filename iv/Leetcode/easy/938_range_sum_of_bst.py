from iv.Binarytree.mytree import MyTree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        mystack = []
        def traversal(node: TreeNode):
            if node:
                if node.left:
                    traversal(node.left)
                mystack.append(node.val)
                if node.right:
                    traversal(node.right)

        traversal(root)
        # print(mystack)
        summ = 0
        for i in mystack:
            # if low <= i <= high:
            #     summ += i
            if i < low:
                continue
            if i > high:
                break
            summ += i
        return summ


root = [10,5,15,3,7,"null",18]; low = 7; high = 15
root = [10,5,15,3,7,13,18,1,"null",6]; low = 6; high = 10
t = MyTree()
rr = t.maketree(root)
s = Solution()
print(s.rangeSumBST(rr, low, high))


