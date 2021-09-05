# 09-05
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, n, m):
  qu = deque([[x, y]])
  hallway[x][y] = 0
  cnt = 1

  while qu:
    x, y = qu.popleft()
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if 0 <= nx < n and 0 <= ny < m and hallway[nx][ny] == 1:
        qu.append([nx, ny])
        hallway[nx][ny] = 0
        cnt += 1
  return cnt


n, m, k = map(int, input().split())
hallway = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
  x, y = map(int, input().split())
  hallway[x-1][y-1] = 1

cnt = 0
for i in range(n):
  for j in range(m):
    if hallway[i][j] == 1:
      cnt = max(cnt, bfs(i, j, n, m))
print(cnt)