class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.right = right
        self.left = left




def creat_cha(index,node):
    print(node.value)
    if (node.value > index) and (node.left == None):
        node.left = Node(index)
    else:
        return creat_cha(index,node.left)
    if (node.value < index) and (node.right == None):
        node.right = Node(index)
    else:
        return creat_cha(index,node.right)

if __name__ == '__main__':

    root = Node(13)
    # print(root.value)
    creat_cha(8,root)
    creat_cha(45,root)
    creat_cha(6,root)






#先把无序表建立成二叉查找树
# def list2tree(q):
#     tree = Node(q[0])
#     a = tree
#     for i in q[1:]:
#         if i < tree.value:
#             if a.left == None:
#                 tree.left = Node(i)
#             else:
#     #             a = a.left
    #     else:
    #         if a.right == None:
    #             tree.right = Node(i)
    #             # a=tree
    #         else:
    #             a = a.right
    # return tree
#
# if __name__ == '__main__':
#     aaa = list2tree([13,45,8,6,4])
#     print(aaa.left.left)





