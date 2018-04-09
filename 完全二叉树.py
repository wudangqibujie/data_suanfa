#完全二叉树的顺序存储
# class Node:
#     def __init__(self,value):
#         self.value = value
import math
class Tree:
    def __init__(self):
        self.tree = []
        self.sub_trees = []
    def add_node(self,node):
        self.tree.append(node)
    def display(self):
        print(self.tree)
    def find_parent_node(self,value):
        if value == self.tree[0]:
            print("No parent node!")
        else:
            in_dex = (self.tree.index(value)-1)/2
            print(in_dex)
            print(self.tree[int(in_dex)])
    def find_right_node(self,value):
        in_de = self.tree.index(value)*2+2
        print(self.tree[in_de])
        return self.tree[in_de]
    def find_left_node(self,value):
        in_de = self.tree.index(value)*2+1
        print(self.tree[in_de])
        return self.tree[in_de]
    def get_height(self):
        print(int(math.log(len(self.tree),2))+1)
    def sub_tree(self,value):
        self.sub_trees.append(value)
        try:
            self.sub_trees.append(self.find_right_node(self.find_right_node("B")))
            self.sub_trees.append(self.find_right_node(value))
        except:
            print(self.sub_trees)






if __name__ == '__main__':
    tr = Tree()
    tr.add_node("A")
    tr.add_node("B")
    tr.add_node("C")
    tr.add_node("D")
    tr.add_node("E")
    # tr.add_node(None)
    tr.add_node("F")
    tr.add_node("G")
    tr.add_node("H")

    tr.display()
    tr.find_parent_node("E")
    tr.find_left_node("C")
    tr.find_right_node("A")
    # tr.find_right_node("C")
    tr.get_height()
    tr.sub_tree("B")




