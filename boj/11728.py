# 08-21
import sys
input = sys.stdin.readline

input().split()
a = list(map(int, input().split()))
a.extend(list(map(int, input().split())))
a.sort()
for e in a:
  print(e, end=' ')