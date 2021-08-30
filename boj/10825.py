# 08-19
import sys
input = sys.stdin.readline

n = int(input())
lst = [input().split() for _ in range(n)]
lst.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for s in lst:
  print(s[0])