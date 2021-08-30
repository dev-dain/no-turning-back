# 08-12
def add(i): l.append(i)

start, end = map(int, input().split())
l = []
for i in range(1, 1000):
  for j in range(i):
    if len(l) >= end: break
    add(i)

print(sum(l[start-1:end]))