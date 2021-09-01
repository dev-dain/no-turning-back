# 09-01
from collections import defaultdict

def preorder(node, visited=[]):
  if node == None: return []
  if node not in visited:
    visited.append(node)
  preorder(tree[node][0])
  preorder(tree[node][1])
  return visited
  
def inorder(node, visited=[]):
  if node == None: return []
  inorder(tree[node][0])
  if node not in visited:
    visited.append(node)
  inorder(tree[node][1])
  return visited
  
def postorder(node, visited=[]):
  if node == None: return []
  postorder(tree[node][0])
  postorder(tree[node][1])
  if node not in visited:
    visited.append(node)
  return visited

n = int(input())
tree = defaultdict(list)
tree_root = None

for _ in range(n):
  root, left, right = input().split()
  if not tree_root:
    tree_root = root
  tree[root].append(left) if left != '.' else tree[root].append(None)
  tree[root].append(right) if right != '.' else tree[root].append(None) 

print(''.join(preorder(tree_root)))
print(''.join(inorder(tree_root)))
print(''.join(postorder(tree_root)))