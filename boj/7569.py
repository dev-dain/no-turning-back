# 08-30
from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, m, h):
  dx = [1, -1, 0, 0, 0, 0]
  dy = [0, 0, -1, 1, 0, 0]
  dz = [0, 0, 0, 0, 1, -1]
  qu = deque(tomatoes)
  # visited 필요 없음
  while qu:
    x, y, z = qu.popleft()

    for i in range(6):
      nx = dx[i] + x
      ny = dy[i] + y
      nz = dz[i] + z
      if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
        if box[nz][nx][ny] == 0:
          box[nz][nx][ny] = box[z][x][y] + 1
          qu.append([nx, ny, nz])
  
  day = 0
  for k in range(h):
    for i in range(n):
      for j in range(m):
        if box[k][i][j] == 0: return -1
        day = max(day, box[k][i][j])
  return day - 1

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
tomatoes = []

for k in range(h):
  for i in range(n):
    for j in range(m):
      if box[k][i][j] == 1:
        tomatoes.append([i, j, k])

print(bfs(n, m, h))