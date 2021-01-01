from iv.Binarytree.mytree import MyTree


arr = [100, 98, 102, 96, 99, "null", "null", "null", 97]
m = MyTree()
root = m.maketree(arr)
res = m.print_tree(root)
print(res)

