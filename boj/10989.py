# 08-19
# from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
  num = int(input())
  if not dic.get(num):
    dic[num] = 1
  else:
    dic[num] += 1

for k, v in sorted(dic.items()):
  for _ in range(v):
    print(k)