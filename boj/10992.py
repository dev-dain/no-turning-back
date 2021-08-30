# 08-18
# 입출력
n = int(input())
star = '* '
for i in range(n):
  if i == 0:
    print('{}{}'.format(' ' * (n-i-1), '*'))
  elif i == n-1:
    print('*'*(n*2-1))
  else:
    print('{0}{1}{2}{1}'.format(' ' * (n-i-1), '*', ' ' * (i*2-1)))