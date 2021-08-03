l = []
for i in range(19):
  l.append(list(map(int, input().split())))
n = int(input())
for i in range(n):
  n, m = map(int, input().split())
  for j in range(19):
    l[n-1][j] = int(not (l[n-1][j]))
    l[j][m-1] = int(not (l[j][m-1]))

for x in l:
  for y in x:
    print(y, end=' ')
  print()