from collections import deque

def solution(priorities, location):
  priorities = deque(priorities)
  orders = deque(list(range(len(priorities))))
  orders[location] = 't' # 아예 여기는 인덱스를 다르게 처리함
  order = 0

  while priorities:
    if priorities[0] == max(priorities):
      order += 1
      if orders[0] == 't':
        return order
      priorities.popleft()
      orders.popleft()
    else:
      priorities.rotate(-1)
      orders.rotate(-1)