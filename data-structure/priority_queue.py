import heapq

class PriorityQueue:
  def __init__(self):
    self._queue = []

  def push(self, item, priority):
    # heappush는 [이터러블, item]을 받음. 여기서는 튜플로 우선순위를 지정함
    heapq.heappush(self._queue, (-priority, item))

  def pop(self):
    return heapq.heappop(self._queue)[-1]

class Item:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return 'Item({0!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('test1'), 1)
q.push(Item('test2'), 4)  # 최우선. 우리는 값이 높은 것이 우선한다고 보지만 heapq는 우선순위 값이 작을수록 우선한다고 봄
q.push(Item('test3'), 3)
print(q.pop())