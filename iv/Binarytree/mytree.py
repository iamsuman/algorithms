class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MyTree:
    def maketree(self, arr: list) -> TreeNode:
        root = TreeNode(arr[0])
        mystack = [root]
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

    def print_tree(self, root: TreeNode):
        my_stack = [root]
        if root:
            res = [root.val]
        else:
            res = []
        while len(my_stack) > 0:
            temp = []
            for node in my_stack:
                print(f"{node.val}", end=" ")
                if node.left:
                    temp.append(node.left)
                    res.append(node.left.val)
                else:
                    res.append("null")
                if node.right:
                    temp.append(node.right)
                    res.append(node.right.val)
                else:
                    res.append("null")
            my_stack = temp
            print("")

        counter = 0
        for i in range(len(res)):
            if res[i] != "null":
                counter = i
        return res[:counter + 1]





