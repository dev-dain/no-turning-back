# 08-19
n = int(input())
mirror = [list(input()) for _ in range(n)]
k = int(input())

for i in range(len(mirror)):
  if k == 1:
    print(''.join(mirror[i]))
  elif k == 2:
    print(''.join(reversed(mirror[i])))
  else:
    print(''.join(mirror[-i-1]))