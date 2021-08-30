# 08-20
from collections import defaultdict
def DFS(g, root, visited=[]):
  visited.append(root)

  for node in g[root]:
    if node not in visited:
      DFS(g, node, visited)
  for node in visited:
    print(node, end=' ')
  print()
  visited.pop()

n = int(input())
g = defaultdict(list)
for i in range(1, n+1):
  g[i] += list(range(i+1, n+1))
for i in range(1, n+1):
  DFS(g, i)