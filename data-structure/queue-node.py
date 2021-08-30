# 노드를 사용한 큐
from node import Node

class Queue:
  def __init__(self):
    self.length = 0
    self.head = None
    self.tail = None

  def enqueue(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
    else:
      self.tail.setNext(new_node)
    self.tail = new_node
    self.length += 1

  def dequeue(self):
    if self.isEmpty():
      return '큐가 비었습니다.'
    return_node = self.head
    self.head = self.head.getNext()
    self.length -= 1
    return return_node.getData()

  def isEmpty(self):
    return not bool(self.length)

  def peek(self):
    if self.isEmpty():
      return '큐가 비었습니다.'
    return self.tail.getData()

  def size(self):
    return self.length

  def traverse(self):
    if self.isEmpty():
      return '큐가 비었습니다.'
    node = self.head
    while node:
      print(node.getData(), end=' ')
      node = node.getNext()
    print('순회 끝')


if __name__ == '__main__':
  queue = Queue()
  print('Is Queue Empty? {}'.format(queue.isEmpty()))
  for i in range(1, 10):
    queue.enqueue(i)
  queue.traverse()
  print(queue.size())
  print(queue.dequeue())
  queue.enqueue(10)
  queue.traverse()