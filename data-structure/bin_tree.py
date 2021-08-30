# 이진 트리 : 노드가 최대 2개의 자식(left, right)을 갖는 자료구조

# 노드 차수 (자식 수)
# 노드 깊이 (루트 노드에서 어떤 노드로 가는 경로 길이). 루트 노드 깊이 0
# 노드 레벨 (노드 깊이 + 1). 루트 노드 레벨 1
# 노드 높이 (한 노드와 단말 노드 사이의 최대 경로 길이)

# perfect binary tree (포화) : 모든 내부 노드가 2개의 자식 노드를 가지고 모든 leaf 노드가 같은 깊이/레벨을 가짐
# complete binary tree (완전) : 마지막 레벨을 제외한 모든 레벨이 완전히 채워진 트리

def BinaryTree(r):
  return [r, [], []]

def insertLeft(root, newBranch):
  t = root.pop(1)
  if len(t) > 1:  # 왼쪽 자식도 자식이 있다면
    root.insert(1, [newBranch, t, []])  # newBranch를 새로운 왼쪽 자식으로 들이고, newBranch의 왼쪽 자식으로 t를 넣음
  else: # 자식 없이 그냥 빈 리스트면 그냥 넣음
    root.insert(1, [newBranch, [], []])
  return root

def insertRight(root, newBranch):
  t = root.pop(2)
  if len(t) > 1:
    root.insert(2, [newBranch, [], t])
  else:
    root.insert(2, [newBranch, [], []])

def getRootVal(root):
  return root[0]

def setRootVal(root, newVal):
  root[0] = newVal

def getLeftChild(root):
  return root[1]

def getRightChild(root):
  return root[2]


r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
print(getRootVal(r))
print(getLeftChild(r))
print(getRightChild(r))