# 08-21
import sys
sys.setrecursionlimit(10**4)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, m, n):
  ground[x][y] = 0

  for a in range(4):
    nx = dx[a] + x
    ny = dy[a] + y
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if ground[nx][ny] == 1:
      dfs(nx, ny, m, n)

t = int(input())
for _ in range(t):
  m, n, k = map(int, input().split())
  ground = [[0 for _ in range(m)] for _ in range(n)]
  veg = [list(map(int, input().split())) for _ in range(k)]
  for x, y in veg:
    ground[y][x] = 1
  
  cnt = 0
  for i in range(n):
    for j in range(m):
      if ground[i][j] == 1:
        dfs(i, j, m, n)
        cnt += 1
  print(cnt)