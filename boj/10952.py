# 08-17
# 입출력
while True:
  a, b = map(int, input().split())
  if a == b and not a:
    break
  print(a+b)