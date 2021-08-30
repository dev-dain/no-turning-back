class Height:
  def __init__(self):
    self.height = 0

class TreeNode:
  # 노드는 값, 레벨, 자식 둘의 정보를 가짐
  def __init__(self, value=None, level=1):
    self.value = value
    self.level = level
    self.left = None
    self.right = None

  def __repr__(self):
    return '{}'.format(self.value)

  def _add_next_node(self, value, level_here=2):
    new_node = TreeNode(value, level_here)
    if not self.value:  # 현재 value가 없는 상태라면
      self.value = new_node # 그냥 현재 값을 새 노드로 바꿔버림
    elif not self.left: # 왼쪽 자식이 없다면
      self.left = new_node  # 새 노드를 왼쪽 자식으로 맞음 (왼쪽부터 채우기 때문에)
    elif not self.right:  # 오른쪽 자식이 없다면
      self.right = new_node # 새 노드를 오른쪽 자식으로 맞음
    else: # 자식이 둘 다 있다면
      self.left = self.left._add_next_node(value, level_here+1) # 레벨을 1 높여서 왼쪽 자식의 자식으로 붙여버림
    return self # 그리고 자기 자신을 return. 자식이 둘 다 있는 경우 유용함

  def _search_for_node(self, value):
    # pre-order로 값 찾기
    if self.value == value: return self # 내가 그 값을 가졌다면 return
    else:
      found = None
      if self.left: # 왼쪽 자식이 있다면
        found = self.left._search_for_node(value)  # 왼쪽 자식에 값 찾기 전가
      if self.right:  # 오른쪽 자식이 있다면
        # 왼쪽에서 찾았는지 확인하고 못 찾았으면 오른쪽 자식에 값 찾기 전가
        found = found or self.right._search_for_node(value) 
      return found  # 뭐 둘 다 없다면 찾으나마나고 if에서 찾았으면 found가 바뀌었을 테니 돌려보냄.

  def _is_leaf(self): # 리프 노드인지 판단
    return not self.left and not self.right

  def _get_max_height(self):  # 노드에서 최대 높이 얻기
    height_l, height_r = 0, 0 # 일단 0으로 시작
    if self.left: # 왼쪽 자식이 있다면 계속 내려가서 높이 얻어오기
      height_l = self.left._get_max_height() + 1 
    if self.right:  # 오른쪽 자식이 있다면 계속 내려가서 높이 얻어오기
      height_r = self.right._get_max_height() + 1
    return max(height_l, height_r)  # 그래서 큰 값(최대 높이) return

  def _is_balanced(self, height=Height()):
    if self.value is None:  # 자식이 없다면 볼 것도 없음
      return True
    
    # 균형 트리인지 확인
    lh = Height()
    rh = Height()

    l, r = True, True
    if self.left:
      l = self.left._is_balanced(lh)  # Height를 내려보내서 왼쪽 자식이 balanced인지 확인
    if self.right:
      r = self.right._is_balanced(rh) # 오른쪽 자식이 balanced인지 확인

    height.height = max(lh.height, rh.height) + 1

    # 만약 왼쪽 자식과 오른쪽 자식의 높이 오차가 1 이하라면
    if abs(lh.height - rh.height) <= 1:
      return l and r  # 위에서 조사한 l, r의 균형 여부 AND

    return False  # 위에서 안 잡히면 False

  def _is_bst(self, left=None, right=None):
    if self.value:
      if left and self.value < left:  # 왼쪽 자식 값이 내 값보다 더 크다면
        return False
      if right and self.value > right:  # 오른쪽 자식 값이 내 값보다 작다면
        return False
      
      # 만약 이 서브트리에서는 True라면 자식들에 대해서도 조사
      l, r = True, True
      if self.left:
        l = self.left._is_bst(left, self.value) # 왼쪽 자식의 자식들에 대해서도 조사
      if self.right:
        r = self.right._is_bst(self.value, right) # 오른쪽 자식의 자식들에 대해서도 조사
    else: # value가 없으면 그냥 True
      return True
      

class BinaryTree:
  def __init__(self):
    self.root = None

  def add_node(self, value):
    if not self.root: # 루트가 없다면 그냥 만들어서 루트 삼으면 되고
      self.root = TreeNode(value)
    else: # 있으면 add_next_node 해서 자식 어딘가에 갖다붙이면 됨
      self.root._add_next_node(value)

  def is_leaf(self, value):
    node = self.root._search_for_node(value)
    if node:  # 이 값을 가진 노드가 있다면
      return node._is_leaf()  # leaf인지 검사
    else: # 없다면 false
      return False
  
  def get_node_level(self, value):
    node = self.root._search_for_node(value)
    if node:  # 이 값을 가진 노드가 있다면
      return node.level # 그냥 레벨 return
    else: # 없다면 false
      return False

  def is_root(self, value):
    return self.root.value == value # root의 value와 주어진 value 비교

  def get_height(self):
    return self.root._get_max_height()  # 트리의 최대 높이 반환

  # 모든 서브 트리 높이 차이가 1 이하인 트리
  def is_balanced(self):
    return self.root._is_balanced() # 균형 트리인지 확인

  def is_bst(self):
    return self.root._is_bst()  # bst인지 확인


if __name__ == '__main__':
  bt = BinaryTree()
  for i in range(1, 10):
    bt.add_node(i)
  print('노드 8은 leaf node입니까? ', bt.is_leaf(8))
  print('노드 8의 레벨은?', bt.get_node_level(8))
  print('노드 10은 루트 노드입니까?', bt.is_root(10))
  print('노드 1은 루트 노드입니까?', bt.is_root(1))
  print('트리 높이는?', bt.get_height())
  print('이진 탐색 트리입니까? ', bt.is_bst())
  print('균형 트리입니까?', bt.is_balanced())