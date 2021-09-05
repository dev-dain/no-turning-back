# 09-04
from itertools import permutations
n = int(input())
a = list(map(int, input().split()))
res_1 = 0
for perm in permutations(a, n):
  res_2 = sum([abs(perm[i] - perm[i+1]) for i in range(len(perm)-1)])
  res_1 = max(res_1, res_2)
print(res_1)