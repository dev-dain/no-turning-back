# 08-18
# 입출력
n = int(input())
for i in range(n):
  star = '* '
  print('{}{}'.format(' '*(n-i-1), star*(i+1)))