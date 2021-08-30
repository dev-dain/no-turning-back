# 08-28
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, n):
  qu = deque([[x, y]])
  visited[x][y] = 1
  i = 0

  while qu:
    print(i, end=' ')
    i += 1
    x, y = qu.popleft()
    # visited[x][y] = 1
    for l in range(4):
      nx = dx[l] + x
      ny = dy[l] + y
      # if nx < 0 or nx >= n or ny < 0 or ny >= n:
      #   continue
      if 0 <= nx < n and 0 <= ny < n:
        if grid[nx][ny] == grid[x][y] and not visited[nx][ny]:
          qu.append([nx, ny])
          visited[nx][ny] = 1

def run_grid(n):
  cnt = 0
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        bfs(i, j, n)
        cnt += 1
  return cnt


n = int(input())
grid = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
cnt_1 = run_grid(n)
# cnt_1 = 0
# for i in range(n):
#   for j in range(n):
#     if not visited[i][j]:
#       bfs(grid, visited, i, j, n)
#       cnt_1 += 1

grid = [['R' if c == 'G' else c for c in row] for row in grid]
# for i in range(n):
#   for j in range(n):
#     if grid[i][j] == 'G':
#       grid[i][j] = 'R'
visited = [[0 for _ in range(n)] for _ in range(n)]
cnt_2 = run_grid(n)
# cnt_2 = 0
# for i in range(n):
#   for j in range(n):
#     if not visited[i][j]:
#       bfs(grid, visited, i, j, n)
#       cnt_2 += 1

print(cnt_1, cnt_2)