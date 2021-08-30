# 08-18
# 입출력
t = int(input())
for i in range(t):
  a, b = map(int, input().split())
  print('Case #{}: {} + {} = {}'.format(i+1, a, b, a+b))