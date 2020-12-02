class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        nodes = []

        def traversal(root, nodes: list):
            if not root:
                return
            if root.left:
                traversal(root.left, nodes)
            nodes.append(root.val)
            if root.right:
                traversal(root.right, nodes)

        traversal(root, nodes)
        # print(nodes)
        mindiff = 2 ** 31 - 1
        for i in range(len(nodes) - 1):
            diff = abs(nodes[i] - nodes[i + 1])
            if mindiff > diff:
                mindiff = diff
        return mindiff



root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
s = Solution()
print(s.getMinimumDifference(root))

