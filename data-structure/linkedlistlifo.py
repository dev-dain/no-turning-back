# 후입선출 연결리스트
from node import Node

# 이 리스트는 추가는 무조건 head 자리에 하고
# 삭제는 노드 인덱스나 값으로 할 수 있음
class LinkedListLIFO:
  def __init__(self):
    # LinkedList는 Node들을 줄줄이 갖게 됨
    self.head = None
    self.length = 0

  # 노드 순회
  def printList(self):
    node = self.head
    while node:
      print(node.getData(), end=' ')
      node = node.getNext()
    print()

  # 노드 삭제
  def delete(self, prev, node):
    self.length -= 1
    if not prev:  # 지금 node가 head 자리라면...
      self.head = node.getNext()  # node의 다음 것을 head로
    else:
      prev.setNext(node.getNext())

  # 노드 추가 (head에 추가함)
  def add(self, value):
    self.length += 1
    self.head = Node(value, self.head)
    
  # 인덱스로 노드 찾기
  def find(self, idx):
    prev = None
    node = self.head
    i = 0
    while node and i < idx:
      prev = node
      node = node.getNext()
      i += 1
    return node, prev, i

  # 값으로 노드 찾기
  def findByValue(self, value):
    prev = None
    node = self.head
    found = False
    while node and not found:
      if node.getData() == value:
        found = True
      else:
        prev = node
        node = node.getNext()
    return node, prev, found

  # 인덱스로 노드 삭제
  def deleteNode(self, idx):
    node, prev, i = self.find(idx)
    if idx == i:
      self.delete(prev, node)
    else:
      print(f'인덱스 {idx}에 해당하는 값을 찾지 못했습니다.')

  # 값으로 노드 삭제
  def deleteNodeByValue(self, value):
    node, prev, found = self.findByValue(value)
    if not found:
      print(f'{value}에 해당하는 값을 찾지 못했습니다.')
    else:
      self.delete(prev, node)


if __name__ == '__main__':
  li = LinkedListLIFO()
  for i in range(1, 5):
    li.add(i)
  li.printList()
  li.deleteNodeByValue(2)
  li.add(15)
  li.printList()