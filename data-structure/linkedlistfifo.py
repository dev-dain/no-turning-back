# 선입선출 연결리스트
from node import Node

class LinkedListFIFO:
  def __init__(self):
    self.length = 0
    self.head = None
    self.tail = None

  def printList(self):
    node = self.head
    while node:
      print(node.getData(), end=' ')
      node = node.getNext()
    print()
  
  def _addFirst(self, value):
    node = Node(value)
    self.length = 1
    self.head = node
    self.tail = node

  # 이게 실행된다는 건 리스트의 최후까지 다 지우는 판국이라는 뜻
  def _deleteFirst(self):
    self.length = 0
    self.head = None
    self.tail = None
    print('연결 리스트가 비었습니다.')

  # 일반적인 경우의 새 노드 추가
  def _add(self, value):
    self.length += 1
    node = Node(value)
    if self.tail:
      self.tail.setNext(node)
    self.tail = node

  # 새 노드 추가
  def addNode(self, value):
    if not self.head: 
      self._addFirst(value)
    else: 
      self._add(value)
    
  def find(self, idx):
    prev = None
    node = self.head
    i = 0
    while node and i < idx:
      prev = node
      node = node.getNext()
      i += 1
    return node, prev, i

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

  def deleteNode(self, idx):
    # 리스트가 비거나 1개밖에 없을 경우
    if not self.head or not self.head.getNext():
      self._deleteFirst()
    else:
      node, prev, i = self.find(idx)
      if i == idx and node: # 그 자리에 노드가 있을 경우
        self.length -= 1
        if i == 0 or not prev:  # head일 경우
          self.head = node.getNext()
          self.tail = node.getNext()
        else:
          prev.setNext(node.getNext())
      else:
        print(f'{idx} 자리에 노드가 없습니다.')
  
  def deleteNodeByValue(self, value):
    if not self.head or not self.head.getNext():
      self._deleteFirst()
    else:
      node, prev, i = self.findByValue(value)
      if node and node.getData() == value:
        self.length -= 1
        if i == 0 or not prev:
          self.head = node.getNext()
          self.tail = node.getNext()
        else:
          prev.setNext(node.getNext())
      else:
        print('값 {}에 해당하는 노드가 없습니다.'.format(value))


if __name__ == '__main__':
  li = LinkedListFIFO()
  for i in range(1, 5):
    li.addNode(i)
  li.printList()
  li.deleteNode(2)
  li.addNode(12)
  li.printList()
  print('모든 노드 삭제')
  for i in range(li.length-1, -1, -1):
    li.deleteNode(i)
  li.printList()