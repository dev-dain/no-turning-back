# 08-26
from collections import deque
import sys
input = sys.stdin.readline

def bfs(box, tomatoes, n, m):
  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]
  qu = deque(tomatoes)
  # visited 필요 없음
  while qu:
    x, y = qu.popleft()

    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if box[nx][ny] == 0:
        box[nx][ny] = box[x][y] + 1
        qu.append([nx, ny])
  
  day = 0
  for i in range(n):
    for j in range(m):
      if box[i][j] == 0: return -1
      day = max(day, box[i][j])
  return day - 1

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
tomatoes = []

for i in range(n):
  for j in range(m):
    if box[i][j] == 1:
      tomatoes.append([i, j])

print(bfs(box, tomatoes, n, m))