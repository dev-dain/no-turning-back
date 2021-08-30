# 08-18
# 입출력
n = int(input())
for i in range(1, n):
  print(('*'*i).rjust(n))
for i in range(n, 0, -1):
  print(('*'*i).rjust(n))