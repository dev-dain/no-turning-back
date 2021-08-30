# 08-19, 08-21
# 스택 생각하고 나중에풀어볼것

import sys
input = sys.stdin.readline

l_cur = list(input().strip())
r_cur = []
m = int(input())
commands = [input().split() for _ in range(m)]

for command in commands:
  if len(command) == 2:
    l_cur.append(command[1])
  elif command[0] == 'L':
    if l_cur:
      r_cur.append(l_cur.pop())
  elif command[0] == 'D':
    if r_cur:
      l_cur.append(r_cur.pop())
  else:
    if l_cur:
      l_cur.pop()
r_cur.reverse()

print(''.join(l_cur)+''.join(r_cur))