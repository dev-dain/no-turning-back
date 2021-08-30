# 08-21
# 완탐 + dfs
def dfs(i, j, n):  
  global cnt
  cnt += 1
  # 일단 방문했으니 이 자리는 0으로 만듦
  arr[i][j] = 0

  for l in range(4):
    # 동서남북 방향 진행을 위해 더하기
    ni = dx[l] + i
    nj = dy[l] + j
    # 만약 map을 벗어나면 그냥 가기
    if ni < 0 or ni >= n or nj < 0 or nj >= n:
      continue
    # 아직 방문 안한 집이 있으면 dfs
    if arr[ni][nj] == 1:
      dfs(ni, nj, n)

# 동서남북
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

apart = []
for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      cnt = 0
      dfs(i, j, n)
      apart.append(cnt)

apart.sort()
print(len(apart))
for a in apart:
  print(a)