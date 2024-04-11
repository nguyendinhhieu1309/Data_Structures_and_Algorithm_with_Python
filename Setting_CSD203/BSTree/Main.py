from Node import  *
from BSTree import  *
tree=BSTree()
tree.addNode(10)
tree.addNode(16)
tree.addNode(14)
tree.addNode(6)
tree.addNode(8)
tree.addNode(7)
tree.addNode(5)
tree.addNode(9)
tree.addNode(19)
tree.addNode(29)
tree.addNode(12)
tree.addNode(13)
tree.addNode(15)

tree.addNode(20)

print(tree.height(tree.root))
#                          10
#                     6          16 
#                5      8    14    19 
#                     7   9 12   15    29
#                              13    20
print("\nBreadFirst Before rotate: ")
tree.breadFirst()

print("\nBreadFirst after rotate: ")
tree.RLRx(19)
tree.breadFirst()

# tree.pre_order(tree.root)
# print()
# tree.deletebyMerging(10)
# print()
# print("height of node %d"%tree.height(tree.findNode(8)))
#tree.deletebyCopy(16)
# p=tree.findNode(16)
# print(tree.rightMost(p).data)
# par=tree.findPar(p)
# if par:
#     print(par.data)
# else:
#     print("no parent found")
# 
#tree.test()
# print("\nPre Order: ")
# tree.pre_order(tree.root)
# print("\nInOrder: ")
# tree.inOrder(tree.root)
# print("\nPostOrder: ")
# tree.postOrder(tree.root)
# print("\nBreadFirst: ")
# tree.breadFirst()
# # n=tree.getNode(19)
# # tree.deleteByCopy(n)
# print("\nBreadFirst after del: ")
# tree.breadFirst()
# h=tree.getNode(10)
# print("\nheight of h is %d"%tree.height(h))
# print("\nDepth of P is %d"%tree.depth(h))
# #1. Duyet theo BreadFirst in ra cac node co 2 con
# #2. Duyet theo BreadFirst in ra cac node co 2 con va gia tri <10
# #2'. Duyet theo BreadFirst in Node thu 3 co 2 con
# 
# #3. Duyet theo InOrder in ra node thu 2 co 2 con va gia tri <10
# 
# #4. Duyet theo PreOder in ra node thu 3 co it nhat 1 con
# 

