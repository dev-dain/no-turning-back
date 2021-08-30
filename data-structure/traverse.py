# 대표적인 DFS 방식의 순회 방법들
# 전위순회 (루트 - L - R)
def preorder(root):
  if root != 0:
    yield root.value
    preorder(root.left)
    preorder(root.right)

# 후위순회 (L - R - 루트)
def postorder(root):
  if root != 0:
    postorder(root.left)
    postorder(root.right)
    yield root.value

# 중위순회 (L - 루트 - R)
def inorder(root):
  if root != 0:
    inorder(root.left)
    yield root.value
    inorder(root.right)