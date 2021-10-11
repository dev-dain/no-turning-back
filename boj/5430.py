# 10-11
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  p = input().strip()
  n = int(input())
  s = input().lstrip('[').rstrip(']\n').split(',')
  direction = 0
  if n:
    s = deque(s)
    if p.count('D') > len(s):
      print('error')
      continue
    for c in p:
      if c == 'R':
        # 이 때마다 뒤집으면 시간초과가 남
        # 그래서 뒤집힌 상태인지 아닌지를 체크하는 게 중요
        direction ^= 1
      else:
        if not s:
          print('error')
          continue
        if direction:
          s.pop()
        else:
          s.popleft()
    if direction:
      s.reverse()
      print(f'[{",".join(s)}]')
    else:
      print(f'[{",".join(s)}]')      
  else:
    if 'D' in p:
      print('error')
      continue
    print('[]')