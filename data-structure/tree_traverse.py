from collections import deque
from bst import BST, BinNode

class BSTwithTraverse(BST):
  def inorder(self):
    cur = self.root
    nodes, stack = [], []
    while stack or cur:
      if cur:
        stack.append(cur)
        cur = cur.left
      else:
        cur = stack.pop()
        nodes.append(cur.value) # 이미 방문한 노드 값
        cur = cur.right
    return nodes

  def preorder(self):
    cur = self.root
    nodes, stack = [], []
    while stack or cur:
      if cur:
        nodes.append(cur.value)
        stack.append(cur)
        cur = cur.left
      else:
        cur = stack.pop()
        cur = cur.right
    return nodes

  def BFS(self):
    cur = self.root
    nodes = []
    queue = deque()
    queue.append(cur)
    while queue:
      cur = queue.popleft()
      nodes.append(cur.value)
      if cur.left:
        queue.append(cur.left)
      if cur.right:
        queue.append(cur.right)
    return nodes

if __name__ == '__main__':
  bst = BSTwithTraverse()
  for i in [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]:
    bst.add_node(i)
  
  print('전위 순회 : ', bst.preorder())
  print('중위 순회 : ', bst.inorder())
  print('BFS : ', bst.BFS())