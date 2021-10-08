# 10-08
from collections import deque

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  priority = deque(list(map(int, input().split())))
  orders = deque(list(range(n)))
  orders[m] = 't' # 아예 여기는 인덱스를 다르게 처리함
  order = 0

  while priority:
    if priority[0] == max(priority):
      order += 1
      if orders[0] == 't':
        print(order)
        break
      priority.popleft()
      orders.popleft()
    else:
      priority.rotate(-1)
      orders.rotate(-1)