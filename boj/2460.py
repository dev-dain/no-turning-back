l = []
for i in range(10):
  leave, take = map(int, input().split())
  if i == 0:
    l.append(take)
  else:
    l.append(l[-1] + take - leave)
print(max(l))