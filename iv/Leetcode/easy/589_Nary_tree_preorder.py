
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list:
        res = []

        def traversal(node: Node):
            if node:
                res.append(node.val)
                if node.children:
                    for child in node.children:
                        traversal(child)

        traversal(root)
        return res

    # def postorder(self, root: 'Node') -> list:
    #     res = []
    #     temp = [root]
    #     while len(temp) > 0:
    #         node = temp.pop(0)
    #         res.append(node.val)
    #         temp.append(node.children)
    #     return res

