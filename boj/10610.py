# 08-31, 09-04
n = list(input())
if '0' not in n:
  print(-1)
else:
  if sum(map(int, n)) % 3:
    print(-1)
  else:
    n.sort(reverse=True)
    print(''.join(n))