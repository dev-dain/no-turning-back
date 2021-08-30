# 08-20
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def DFS(g, root, visited=[], cnt=0):
  visited.append(root)
  cnt = 0

  # root가 가진 모든 node에 대해 루프 돌기
  for node in g[root]:
    if node not in visited:
      cnt = DFS(g, node, visited)
  cnt += 1
  return cnt

def BFS(g, root, visited):
  qu = deque([root])

  while qu:
    node = qu.popleft()
    if not visited[node]:
      visited[node] = 1
      qu += g[node]
      
n, m = map(int, input().split())
g = defaultdict(list)
# 그래프가 어떻게 연결되어 있는지 모르기 때문에
# visited를 vertex 개수만큼 만들어놓음 (False로)
visited = [0 for _ in range(n+1)]

for _ in range(m):
  u, v = map(int, input().split())
  g[u].append(v)
  g[v].append(u)

cnt = 0
# 그리고 visited만큼 돌려서
# false이면 연결이 안된 그래프의 시작이므로 cnt 늘리기
for i in range(1, n+1):
  if visited[i] == 0:
    cnt += 1
    BFS(g, i, visited)
print(cnt)