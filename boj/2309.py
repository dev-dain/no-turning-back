# 08-12
# https://www.acmicpc.net/problem/2309

l = sorted([int(input()) for _ in range(9)])
diff = sum(l) - 100
for i in range(len(l)-1):
  for j in range(i+1, len(l)):
    if l[i] + l[j] == diff:
      x, y = l[i], l[j]
      l.remove(x)
      l.remove(y)
      break
for x in l: print(x)