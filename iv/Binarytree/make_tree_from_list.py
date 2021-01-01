class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Mytree:
    def maketree(self, arr: list):
        root = TreeNode(arr[0])
        mystack = []
        mystack.append(root)
        nl = []
        i = 0
        while len(mystack) > 0:
            node = mystack.pop(0)
            i += 1
            if i < len(arr):
                if arr[i] != "null":
                    node.left = TreeNode(arr[i])
                    mystack.append(node.left)
            else:
                break
            i += 1
            if i < len(arr):
                if arr[i] != "null":
                    node.right = TreeNode(arr[i])
                    mystack.append(node.right)
            else:
                break
        # print(root.left.val)
        return root


arr = [20, 8, 22, 4, 12, "null", "null", "null", "null", 10, 14]
s = Mytree()
root = s.maketree(arr)
print(root.val)
