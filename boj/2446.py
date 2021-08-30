# 08-18
# 입출력
n = int(input())
for i in range(n, 1, -1):
  print('{}{}'.format(' '*(n-i), '*'*((i*2)-1)))
for i in range(1, n+1):
  print('{}{}'.format(' '*(n-i), '*'*((i*2)-1)))
