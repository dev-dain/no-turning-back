# 08-27
import sys
input = sys.stdin.readline

s = [0] * 21
m = int(input())
for _ in range(m):
  command = input().split()
  if command[0] == 'all':
    s = [1] * 21
  elif command[0] == 'empty':
    s = [0] * 21
  else:
    n = int(command[1])
    if command[0] == 'add':
      s[n] = 1
    elif command[0] == 'remove':
      s[n] = 0
    elif command[0] == 'check':
      print(s[n])
    else:
      s[n] ^= 1