from collections import deque

def solution(priorities, location):
  qu = deque(priorities)
  max_idx = qu.index(max(qu))
  while qu:
    print(location)
    if qu[0] != max(qu):
      qu.rotate(-max_idx)
      location -= max_idx
    qu.popleft()
    max_idx = qu.index(max(qu))

solution([2, 1, 3, 2], 2)