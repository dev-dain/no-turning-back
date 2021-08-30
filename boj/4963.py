# 08-21
# recursion error로 limit 늘려주기
import sys
sys.setrecursionlimit(10**4)

def dfs(i, j, h, w):
  m[i][j] = 0

  for n in range(8):
    ni = dx[n] + i
    nj = dy[n] + j
    if ni < 0 or ni >= h or nj < 0 or nj >= w:
      continue
    if m[ni][nj] == 1:
      dfs(ni, nj, h, w)  

while True:
  w, h = map(int, input().split())
  if w == h and w == 0: 
    break

  m = [list(map(int, input().split())) for _ in range(h)]
  dx = [1, -1, 0, 0, 1, 1, -1, -1]
  dy = [0, 0, -1, 1, -1, 1, -1, 1]
  cnt = 0
  
  for i in range(h):
    for j in range(w):
      if m[i][j] == 1:
        dfs(i, j, h, w) 
        cnt += 1
  print(cnt)