# 08-20
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque([])
for _ in range(n):
  s = input().split()
  c = s[0]

  if c == 'push_front':
    d.appendleft(int(s[1]))
  elif c == 'push_back':
    d.append(int(s[1]))
  elif c == 'pop_front':
    print(d.popleft()) if d else print(-1)
  elif c == 'pop_back':
    print(d.pop()) if d else print(-1)
  elif c == 'size':
    print(len(d))
  elif c == 'empty':
    print(0) if len(d) else print(1)
  elif c == 'front':
    print(d[0]) if d else print(-1)
  else:
    print(d[-1]) if d else print(-1)