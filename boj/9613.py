# 09-02
from itertools import combinations

def gcd(x, y):
  return x if y == 0 else gcd(y, x%y)

t = int(input())
for _ in range(t):
  n, *arr = map(int, input().split())
  res = 0
  for combi in combinations(arr, 2):
    res += gcd(*combi)
  print(res)