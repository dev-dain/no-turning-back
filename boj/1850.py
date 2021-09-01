# 09-01
a, b = map(int, input().split())
while a:
  b = b % a
  a, b = b, a
print('1' * b)