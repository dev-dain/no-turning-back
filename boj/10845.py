# 08-19
# 이거 18258이랑 똑같은데..?

import sys
input = sys.stdin.readline
from collections import deque

queue = deque()
idx = 0
n = int(input())
# 리스트 컴프리헨션으로 고쳐서 했더니 시간초과 안뜸
for _ in range(n):
  order = input().split()
  if len(order) != 1:
    queue.append(int(order[1]))
  elif order[0] == 'pop':
    print(queue.popleft()) if len(queue) else print(-1)
  elif order[0] == 'size':
    print(len(queue))
  elif order[0] == 'empty':
    print(0) if len(queue) else print(1)
  elif order[0] == 'front':
    print(queue[0]) if len(queue) else print(-1)
  elif order[0] == 'back':
    print(queue[-1]) if len(queue) else print(-1)