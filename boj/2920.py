# 08-19
n = list(map(int, input().split()))
if n == list(range(1, 9)):
  print('ascending')
elif n == list(range(8, 0, -1)):
  print('descending')
else:
  print('mixed')
