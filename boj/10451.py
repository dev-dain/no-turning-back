# 08-20
from collections import defaultdict

def dfs(g, root, visited=[]):
  visited[root] = 1

  for node in g[root]:
    if not visited[node]:
      dfs(g, node, visited)


t = int(input())
for _ in range(t):
  n = int(input())
  c = list(map(int, input().split()))
  g = defaultdict(list)
  visited = [0] * (n+1)
  cnt = 0

  for idx, val in enumerate(c):
    g[idx+1].append(val)
  for idx, val in enumerate(c):
    if not visited[idx+1]:
      cnt += 1
      dfs(g, idx+1, visited)
  
  print(cnt)
