# 08-21
from collections import defaultdict

def dfs(g, root, visited=[]):
  visited.append(root)

  for node in g[root]:
    if node not in visited:
      visited = dfs(g, node, visited)
  return visited

n, e = [int(input()) for _ in range(2)]
g = defaultdict(list)
for _ in range(e):
  a, b = input().split()
  g[a].append(b)
  g[b].append(a)
visited = dfs(g, '1')
print(len(visited)-1)