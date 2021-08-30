# 08-19

from collections import deque
n, k = map(int, input().split())
qu = deque(range(1, n+1))
lst = []

while qu:
  qu.rotate(-k+1)
  lst.append(qu.popleft())
lst = list(map(str, lst))
print(f"<{', '.join(lst)}>")