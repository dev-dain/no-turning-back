# 08-17
from collections import deque

n = int(input())
qu = deque(range(1,n+1))

while len(qu) > 1:
  qu.popleft()
  qu.rotate(-1)
print(qu[0])