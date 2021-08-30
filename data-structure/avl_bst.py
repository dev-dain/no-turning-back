from bintree import TreeNode, BinaryTree

class NodeAVL(TreeNode):
  def __init__(self, value=None, height=1):
    self.value = value
    self.height = height
    self.left = None
    self.right = None

  def insert(self, value):
    # 1. bst 트리 노드 삽입
    new_node = NodeAVL(value)
    if value < self.value:
      self.left = self.left and self.left.insert(value) \
        or new_node
    elif value > self.value:
      self.right = self.right and self.right.insert(value) \
        or new_node
    else:
      raise Exception('중복 노드를 허용하지 않습니다')

    # 일단 삽입은 삽입대로 하고 값만 가져가서 
    # 회전 메소드에서 높이 설정
    return self.rotate(value)

  def rotate(self, value):
    # 2. 조상 노드 높이 갱신
    self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))

    # 3. 균형도 구하기 (왼쪽 트리 높이 - 오른쪽 트리 높이)
    balance = self.get_balance()

    # 4. 트리 균형이 맞지 않을 경우 회전
    if balance > 1:
      # case 1. LL - Left Left
      if value < self.left.value:
        return self.right.rotate()

      # case 2. LR - Left Right
      elif value > self.left.value:
        self.left = self.left.left_rotate()
        return self.right_rotate()
      
    elif balance < -1:
      # case 3. RR - Right Right
      if value > self.right.value:
        return self.left_rotate()

      # case 4. RL - Right Left
      elif value < self.right.value:
        self.right = self.right.right_rotate()
        return self.left_rotate()

    return self

  def left_rotate(self):
    # 여기서 self는 y (루트)
    x = self.right
    T2 = x.left

    # 회전한 후
    x.left = self
    self.right = T2

    # 높이 갱신
    self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
    x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

    # 새로운 루트 노드 반환
    return x

  def right_rotate(self):
    # 여기서 self는 x (루트)
    y = self.left
    T2 = y.right

    # 회전한 후
    y.right = self
    self.left = T2

    # 높이 갱신
    self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
    y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    return y

  def get_height(self, node):
    if not node:
      return 0

    return node.height

  def get_balance(self):
    return self.get_height(self.left) - self.get_height(self.right)

  def get_min_value_node(self, node):
    if node is None or node.left is None:
      return node

    return self.get_min_value_node(node.left)

  def delete(self, value):
    # 이진 탐색 트리 노드 삭제
    if value < self.value:
      self.left = self.left and self.left.delete(value)
    elif value > self.value:
      self.right = self.right and self.right.delete(value)
    else:
      if self.left is None:
        temp = self.right
        self = None
        return temp
      elif self.right is None:
        temp = self.left
        self = None
        return temp

      temp = self.get_min_value_node(self.right)
      self.value = temp.value
      self.right = self.right and self.right.delete(temp.value)

    if self is None:
      return None

    return self.rotate(value)


class AVLTree(BinaryTree):
  def __init__(self):
    self.root = None

  def insert(self, value):
    if not self.root:
      self.root = NodeAVL(value)
    else:
      self.root = self.root.insert(value)

  def delete(self, value):
    self.root = self.root.delete(value)

def preorder(root):
  if root:
    print('({0}, {1})'.format(root.value, root.height-1), end=' ')
    if root.left:
      preorder(root.left)
    if root.right:
      preorder(root.right)


if __name__ == '__main__':
  myTree = AVLTree()
  for i in range(10, 100, 10):
    myTree.insert(i)
  
  print('트리 높이는? ', myTree.get_height())
  print('이진 트리입니까? ', myTree.is_bst())
  print('균형 트리입니까? ', myTree.is_balanced())
  preorder(myTree.root)