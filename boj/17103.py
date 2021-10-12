# 10-12
import sys
input = sys.stdin.readline

table = [0, 0] + [1] * 999999
for i in range(len(table)):
  if table[i]:
    for j in range(i*2, len(table), i):
      table[j] = 0

t = int(input())
for _ in range(t):
  n = int(input())
  cnt = 0

  for i in range(2, (n//2)+1):
    if table[i] and table[n-i]:
      cnt += 1
  print(cnt)