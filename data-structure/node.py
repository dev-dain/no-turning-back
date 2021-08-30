# 연결리스트 노드
# 노드는 데이터와 next에 대한 정보만 가짐
class Node:
  def __init__(self, value=None, pointer=None):
    self.value = value
    self.pointer = pointer

  def getData(self):
    return self.value

  def getNext(self):
    return self.pointer
  
  def setData(self, value):
    self.value = value
  
  def setNext(self, pointer):
    self.pointer = pointer


if __name__ == '__main__':
  L = Node('a', Node('b', Node('c', Node('d'))))
  print(L.getData())
  L.getNext().setData('B')
  print(L.getNext().getNext().getData())
  print(L.getNext().getData())