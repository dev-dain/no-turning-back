# 08-20
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  if n == 0: print('1 0')
  elif n == 1: print('0 1')
  else:
    table = [0] * (n+1)
    table[0] = [1, 0]
    table[1] = [0, 1]
  
    for i in range(2, n+1):
      table[i] = [table[i-2][0] + table[i-1][0], table[i-2][1] + table[i-1][1]]
    print(table[n][0], table[n][1])