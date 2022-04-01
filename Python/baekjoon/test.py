# class Node:
#     value = None
#     left = None
#     right = None
#     parent = None
#
#     def __init__(self, value, parent=None):
#         self.value = value
#         self.parent = parent
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, value, child_side=None, parent=None):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             node = Node(value, parent)
#             if child_side == 'l':
#                 parent.left = node
#             elif child_side == 'r':
#                 parent.right = node
#
#     def inOrderTraverse(self, node):
#         if node.left is not None:
#             self.inOrderTraverse(node.left)
#         print(node.value, end=' ')
#         if node.right is not None:
#             self.inOrderTraverse(node.right)
#
#     def preOrder(self, node):
#         print(node.value, end=' ')
#         if node.left is not None:
#             self.preOrder(node.left)
#         if node.right is not None:
#             self.preOrder(node.right)
#
#     def postOrder(self, node):
#         if node.left is not None:
#             self.postOrder(node.left)
#         if node.right is not None:
#             self.postOrder(node.right)
#         print(node.value, end=' ')
#
# tree = Tree()
#
# tree.insert(20)
# pnode = tree.root
# tree.insert(60, 'l', pnode)
# tree.insert(30, 'r', pnode)
#
# pnode = pnode.left
# tree.insert(2, 'l', pnode)
# tree.insert(1, 'r', pnode)
#
# pnode = pnode.right
# tree.insert(6, 'l', pnode)
#
# pnode = tree.root.right
# tree.insert(5, 'l', pnode)
#
# pnode = pnode.left
# tree.insert(9, 'r', pnode)
#
# pnode = pnode.parent
# tree.insert(7, 'r',pnode)
#
# pnode = pnode.right
# tree.insert(10, 'l', pnode)
# tree.insert(8, 'r', pnode)
#
# pnode = pnode.right
# tree.insert(4, 'r', pnode)
#
# print("in Order")
# tree.inOrderTraverse(tree.root)
# print()
# print("\npost Order")
# tree.postOrder(tree.root)
# print()
# print("\npre Order")
# tree.preOrder(tree.root)
# #
# 12
# 2 60 6 1 20 5 9 30 10 7 8 4
# 2 6 1 60 9 5 10 4 8 7 30 20
# # 20 60 2 1 6 30 5 9 7 10 8 4









#-----------------------------------------------------------------

# def sort(arr, left, right):
#     mid = left + (right - left)//2 + 1
#     if(right-left < 1):
#         return arr[left:right+1]
#     left_arr = sort(arr, left, mid-1) #left ~ mid
#     right_arr = sort(arr, mid, right) #mid+1 ~ right
#
#     #merge
#     res = []
#     while(True):
#         if(left_arr[0] > right_arr[0]):
#             res.append(right_arr.pop(0))
#         elif(left_arr[0] == right_arr[0]):
#             res.append(right_arr.pop(0))
#             res.append(left_arr.pop(0))
#         else:
#             res.append(left_arr.pop(0))
#
#         if(len(left_arr) == 0):
#             res += right_arr
#             break
#         if(len(right_arr) == 0):
#             res += left_arr
#             break
#     return res
#
# test = [6, 30, 7, 5, 124, 4, 60, 9, -13]
# sorted_test = sort(test, 0, len(test)-1)
# print(sorted_test)


#----------------------------------------------------------------
from collections import Counter

nums = [0, 0, -1]
N = 3

counter = Counter(nums).most_common(2)
print(counter)

# if(N > 1):
#     mode = counter[0] if counter[0] > counter[1] else counter[1]
# else:
#     mode = nums[0]


