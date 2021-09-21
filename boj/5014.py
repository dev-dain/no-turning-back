# 09-21
from collections import deque
def bfs():
  # 흠.. visited를 관리해줘야 한다
  # 같은 층을 빙빙 돌면 안 되니까
  global f, s, g, u, d
  qu = deque([[s, 0]])
  visited = {s}

  while qu:
    cur, cnt = qu.popleft()
    if cur == g:
      return cnt
    if cur - d > 0 and cur - d not in visited:
      qu.append([cur-d, cnt+1])
      visited.add(cur-d)
    # elif가 아니라 if로 가야된다 업다운 둘 다 가능하면 둘 다 해봐야함
    if cur + u <= f and cur + u not in visited:
      qu.append([cur+u, cnt+1])
      visited.add(cur+u)

  # 만약 갈 수 없는 층이거나(지하를 뚫고 가거나 옥상으로 가거나) 
  # 계속 같은 층을 빙빙 돌고 있다면(visited에 포함돼 있다면) 실패
  # 10 1 5 3 3
  return 'use the stairs'

f, s, g, u, d = map(int, input().split())
print(bfs())


'''
from collections import deque
def bfs():
  global f, s, g, u, d
  if s == g: return 0
  elif (s > g and d == 0) or (s < g and u == 0):
    return "use the stairs"
  qu = deque([[s, 0]])

  while qu:
    cur, cnt = qu.popleft()
    if cur == g:
      return cnt
    if cur > g:
      if cur-d > 0:
        qu.append([cur-d, cnt+1])
      else:
        qu.append([cur+u, cnt+1])
    elif cur < g:
      if cur+u <= f:
        qu.append([cur+u, cnt+1])
      else:
        qu.append([cur-d, cnt+1])
      

f, s, g, u, d = map(int, input().split())
print(bfs())
'''
