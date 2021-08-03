h, w = map(int, input().split())
lst = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())
for _ in range(n):
  l, d, x, y = map(int, input().split())
  if d == 0:
    for i in range(l):
      lst[x-1][y-1+i] = int(not (lst[x-1][y-1+i]))
  else:
    for i in range(l):
      lst[x-1+i][y-1] = int(not(lst[x-1+i][y-1]))

for x in lst:
  for y in x:
    print(y, end=' ')
  print()