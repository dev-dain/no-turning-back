# 08-14

m, n = map(int, input().split())
lst = [True] * (n+1)
lst[1] = False
for i in range(2, int(n**1/2)+1):
  if lst[i] == True:
    for j in range(i*2, n+1, i):
      lst[j] = False

lst = [x[0] for x in filter(lambda x : True if x[1] else False, enumerate(lst)) if x[0] >= m]
for e in lst:
  print(e)