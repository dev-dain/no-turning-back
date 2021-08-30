# 08-19
def calc(n, money, cnt):
  while n >= money:
    n -= money
    cnt += 1
  return n, cnt

n = 1000 - int(input())
cnt = 0
for money in (500, 100, 50, 10, 5, 1):
  n, cnt = calc(n, money, cnt)
print(cnt)