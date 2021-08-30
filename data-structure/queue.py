class Queue:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return not bool(self.items)
  
  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    try:
      return self.items.pop(0)
    except:
      print('큐가 비었습니다.')

  def size(self):
    return len(self.items)

  def peek(self):
    try:
      return self.items[-1]
    except:
      print('큐가 비었습니다.')

  def __repr__(self):
    return repr(self.items)

  def traverse(self):
    for i in range(len(self.items)):
      print('{} id : {}', self.items[i], id(self.items[i]))


if __name__ == '__main__':
  queue = Queue()
  print('Is Queue Empty? {}'.format(queue.isEmpty()))
  for i in range(1, 10):
    queue.enqueue(i)
  print(queue)
  print(queue.size())
  print(queue.dequeue())
  print(queue)
  print(queue.traverse())