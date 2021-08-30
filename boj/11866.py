from collections import deque

n, k = map(int, input().split())
qu = deque(range(1, n+1))
lst = []
while qu:
  qu.rotate(-k)
  lst.append(str(qu.pop()))
print(f'<{", ".join(lst)}>')