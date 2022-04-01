#-----------------------------------------------------------------
#
# import sys
#
# inputs = []
# line = sys.stdin.readline()
# while line!='':
#     if line == '\n':
#         break
#     node = int(line)
#     inputs.append(node)
#     line = sys.stdin.readline()
#
#
# tree = [-1 for i in range(2 ** len(inputs))]
#
# def insert(tree, value, parent_index=None):
#     if parent_index is None:
#         parent_index = 0
#     if value > tree[parent_index]:
#         if tree[parent_index * 2 + 1] == -1 :
#             tree[parent_index * 2 + 1] = value
#             return
#         else:
#             insert(tree, value, parent_index * 2 + 1)
#     if value < tree[parent_index]:
#         if tree[parent_index * 2] == -1:
#             tree[parent_index * 2] = value
#             return
#         else:
#             insert(tree, value, parent_index * 2)
#
# def postOrderTraverse(tree, nodeIndex):
#     if tree[nodeIndex * 2] != -1:
#         postOrderTraverse(tree, nodeIndex * 2)
#     if tree[nodeIndex * 2 + 1] != -1:
#         postOrderTraverse(tree, nodeIndex * 2 + 1)
#     print(tree[nodeIndex])
#
# for i in range(len(inputs)):
#     insert(tree, inputs[i])
#
# postOrderTraverse(tree, 1)

# codes above - memory overflow



#-----------------------------------------------------------------
#
# import sys
# sys.setrecursionlimit(int(1e9))
# inputs = []
# line = sys.stdin.readline()
# while line!='':
#     if line == '\n':
#         break
#     node = int(line)
#     inputs.append(node)
#     line = sys.stdin.readline()
#
# class Node:
#     value = None
#     parentNode = None
#     LHS = None
#     RHS = None
#     def __init__(self, value, parentNode=None):
#         self.value = value
#         self.parentNode = parentNode
#
# class Tree:
#     root = None
#     len = 0
#     def __init__(self, node=None):
#         self.root = node
#
#     def insert(self, value, parent=None):
#         if parent is None:
#             if self.root is None:
#                 self.root = Node(value)
#                 self.len += 1
#                 return
#             parent = self.root
#         if value == parent.value:
#             return
#         if value > parent.value:
#             if parent.RHS is None:
#                 parent.RHS = Node(value, parent)
#                 self.len += 1
#                 return
#             else:
#                 self.insert(value, parent.RHS)
#         if value < parent.value:
#             if  parent.LHS is None:
#                 parent.LHS = Node(value, parent)
#                 self.len += 1
#                 return
#             else:
#                 self.insert(value, parent.LHS)
#
#     def postOrderTrav(self, node=None):
#         if node is None:
#             node = self.root
#         if node.LHS is not None:
#             self.postOrderTrav(node.LHS)
#         if node.RHS is not None:
#             self.postOrderTrav(node.RHS)
#         print(node.value)
#
# tree = Tree()
#
# for i in inputs:
#     tree.insert(i)
#
# tree.postOrderTrav(tree.root)
#
#
# -> time over..



#-----------------------------------------------------------------

import sys
sys.setrecursionlimit(int(1e9))
inputs = []
line = sys.stdin.readline()
while line!='':
    if line == '\n':
        break
    node = int(line)
    inputs.append(node)
    line = sys.stdin.readline()

def dfs(tree, start, end):
    if start > end:
        return
    Rs = end + 1
    for i in range(start+1, end+1):
        if tree[i] > tree[start]:
            Rs = i
            break

    dfs(tree, start+1, Rs-1)
    dfs(tree, Rs, end)
    print(tree[start])

dfs(inputs, 0, len(inputs)-1)