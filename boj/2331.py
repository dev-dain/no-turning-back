# 08-31
a, p = map(int, input().split())
d = []
while a not in d:
  d.append(a)
  a = list(str(d[-1]))
  a = sum([int(c) ** p for c in a])
print(len(d[:d.index(a)]))