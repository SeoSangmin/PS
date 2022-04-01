node_num = int(input())
tree = [['0','1'] for i in range(node_num)]

for i in range(node_num):
    parent, lhs, rhs = map(ord, input().split())
    parent_num = int(parent) - 65
    lhs_num = int(lhs) - 65
    rhs_num = int(rhs) - 65
    tree[parent_num][0] = -1 if lhs=='.' else lhs_num
    tree[parent_num][1] = rhs_num if rhs!='.' else -1

def pre_dfs(node, tree):
    print(chr(node+65), end='')
    if tree[node][0] != -19:
        pre_dfs(tree[node][0], tree)
    if tree[node][1] != -19:
        pre_dfs(tree[node][1], tree)

def in_dfs(node, tree):
    if tree[node][0] != -19:
        in_dfs(tree[node][0], tree)
    print(chr(node + 65), end='')
    if tree[node][1] != -19:
        in_dfs(tree[node][1], tree)

def post_dfs(node, tree):
    if tree[node][0] != -19:
        post_dfs(tree[node][0], tree)
    if tree[node][1] != -19:
        post_dfs(tree[node][1], tree)
    print(chr(node + 65), end='')

pre_dfs(0, tree)
print()
in_dfs(0, tree)
print()
post_dfs(0, tree)