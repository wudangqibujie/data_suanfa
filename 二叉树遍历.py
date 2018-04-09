class Node:
    def __init__(self,value = None,left = None,right = None):
        self.value = value
        self.left = left
        self.right = right
def pre_order(tree):
    if tree == None:
        return
    print(tree.value)
    pre_order(tree.left)
    pre_order(tree.right)
def mid_order(tree):
    if tree == None:
        return
    mid_order(tree.left)
    print(tree.value)
    mid_order(tree.right)
def post_order(tree):
    if tree == None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.value)
def level_order(tree):
    if tree == None:
        return
    q = []
    q.append(tree)
    while q:
        current = q.pop(0)
        print(current.value)
        if current.left != None:
            q.append(current.left)
        if current.right != None:
            q.append(current.right)

class Tree:
    def __init__(self):
        self.tree = []
    def add_node(self):
        pass

if __name__ == '__main__':
    e = Node("E")
    f = Node("F")
    g = Node("G")
    h = Node("H")
    d = Node("D",g,h)
    b = Node("B",d,e)
    c = Node("C",f)
    a = Node("A",b,c)
    # pre_order(a)
    # mid_order(a)
    # post_order(a)
    level_order(a)
