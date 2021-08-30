# 08-20
from collections import deque, defaultdict
def DFS(graph, root, visited=[]):
  visited.append(root)

  for node in graph[root]:
    if node not in visited:
      DFS(graph, node, visited)

  return list(map(str, visited))


def BFS(graph, root):
  visited = []
  qu = deque([root])

  while qu:
    node = qu.popleft()
    if node not in visited:
      visited.append(node)
      # qu append가 아님!
      qu += graph.get(node)
  return list(map(str, visited))

n, m, v = map(int, input().split())
# defaultdict로 하면 빈 부분은 자동으로 defaultdict가 됨
graph = defaultdict(list)
for _ in range(m):
  s, e = map(int, input().split())
  if graph.get(s):
    graph[s].append(e)
  else:
    graph[s] = [e]
  if graph.get(e):
    graph[e].append(s)
  else:
    graph[e] = [s]
  for val in graph.values():
    val.sort()
  # 정렬까지 해야함 까다롭네..

print(' '.join(DFS(graph, v)))
print(' '.join(BFS(graph, v)))