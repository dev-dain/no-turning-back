# 트리를 구현하는 가장 간단한 방법은 중첩 리스트지만 다루기 불편
# 클래스가 있는 것이 차라리 나음

class Tree:
  def __init__(self, value=None, children=None):
    self.value = value
    self.children = children
    if self.children is None:
      self.children = []
  
  def __repr__(self, level=0):
    ret = '\t'*level + repr(self.value) + '\n'
    for child in self.children:
      ret += child.__repr__(level+1)
    return ret

st = Tree('a', [
  Tree('b', [
    Tree('d'),
    Tree('e')
  ]),
  Tree('c', [
    Tree('h'),
    Tree('g')
  ])
])
print(st)