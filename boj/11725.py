# 09-04
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def dfs(parent, visited=[]):
  visited.append(parent)
  for node in tree[parent]:
    if not parents[node]:
      parents[node] = parent
    if node not in visited:
      dfs(node, visited)

def bfs(parent):
  qu = deque([parent])
  visited = [0] * (n+1)
  visited[parent] = 1

  while qu:
    parent = qu.popleft()
    for node in tree[parent]:
      if not parents[node]:
        parents[node] = parent
      if not visited[node]:
        qu.append(node)
        visited[node] = 1

n = int(input())
tree = defaultdict(list)
parents = [0] * (n+1)
for _ in range(n-1):
  n1, n2 = map(int, input().split())
  tree[n1].append(n2)
  tree[n2].append(n1)
bfs(1)
for i in range(2, n+1):
  print(parents[i])