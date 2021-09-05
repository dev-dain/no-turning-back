# 09-04
# 꼭 리뷰하기. 다리 건설 부분에서 최소 길이를 찾는 방법을 못 찾고 막혔음
from collections import deque

def bfs(i, j, n, cnt):
  qu = deque([[i, j]])
  board[i][j] = cnt

  while qu:
    x, y = qu.popleft()
    for k in range(4):
      nx = dx[k] + x
      ny = dy[k] + y
      if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
        qu.append([nx, ny])
        board[nx][ny] = cnt

def build_bridge(num, n):
  # map에서 나올 수 있는 최대 다리 길이
  global bridge
  # 거리가 저장될 dist 배열
  dist = [[-1 for _ in range(n)] for _ in range(n)]
  qu = deque()

  # 해당 섬 영역은 거리를 0으로 초기화
  for i in range(n):
    for j in range(n):
      if board[i][j] == num:
        qu.append([i, j])
        dist[i][j] = 0
  
  while qu:
    x, y = qu.popleft()
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if 0 <= nx < n and 0 <= ny < n:
        # 0도 아니고 num도 아니라면 다른 섬에 닿은 것임
        if board[nx][ny] != 0 and board[nx][ny] != num:
          # bridge가 완성되어 다른 섬에 도착했으므로 최소 길이와 비교하고 그냥 return
          # global이라 딱히 값을 return할 필요는 없음
          bridge = min(bridge, dist[x][y])
          print(dist)
          return
        # 바다이고 아직 영역을 넓히지 않은 곳이라면..
        if board[nx][ny] == 0 and dist[nx][ny] == -1:
          dist[nx][ny] = dist[x][y] + 1
          qu.append([nx, ny])


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
bridge = n ** 2
cnt = 2

for i in range(n):
  for j in range(n):
    if board[i][j] == 1:
      bfs(i, j, n, cnt)
      cnt += 1
# cnt(섬의 개수)만큼 다리 건설
for i in range(2, cnt):
  build_bridge(i, n)
print(bridge)
