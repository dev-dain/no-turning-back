# 08-18
# 입출력
n = int(input())
for i in range(1, n):
  print('{0}{1}{0}'.format('*'*i, ' '*((2*n)-(2*i))))
for i in range(n, 0, -1):
  print('{0}{1}{0}'.format('*'*i, ' '*((2*n)-(2*i))))