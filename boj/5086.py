# 08-20
while True:
  n, m = map(int, input().split())
  if n == m and n == 0:
    break
  if m % n == 0: print('factor')
  elif n % m == 0: print('multiple')
  else: print('neither')