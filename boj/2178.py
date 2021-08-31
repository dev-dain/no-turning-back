# 08-31
import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(n, m):
  qu = deque([[0, 0]])
  
  while qu:
    x, y = qu.popleft()
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
        qu.append([nx, ny])
        if nx == n-1 and ny == m-1:
          maze[nx][ny] = min(maze[x][y] + 1, maze[nx][ny]) if maze[nx][ny] != 1 else maze[x][y] + 1
        else:
          maze[nx][ny] = maze[x][y] + 1
    

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

bfs(n, m)
print(maze[n-1][m-1])