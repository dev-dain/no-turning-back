# 09-01
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j, m, n):
  qu = deque([[i, j]])
  visited[i][j] = 1
  cnt = 1

  while qu:
    i, j = qu.popleft()
    for k in range(4):
      nx = dx[k] + i
      ny = dy[k] + j
      if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] \
        and soldiers[nx][ny] == soldiers[i][j]:
        qu.append([nx, ny])
        visited[nx][ny] = 1
        cnt += 1
  return cnt

n, m = map(int, input().split())
soldiers = [list(input()) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

w = b = 0
for i in range(m):
  for j in range(n):
    if not visited[i][j]:
      if soldiers[i][j] == 'W':
        w += bfs(i, j, m, n) ** 2
      else:
        b += bfs(i, j, m, n) ** 2

print(w, b)